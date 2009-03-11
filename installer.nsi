; installer.nsi
;
!include "WordFunc.nsh"
;--------------------------------

; The name of the installer
Name "PyTong installer"

; The file to write
OutFile "dist/PyTong_installer_0.1.exe"

; The default installation directory
InstallDir $PROGRAMFILES\PyTong

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\PyTong" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel user

; Icon for the installer
Icon "icons\icon32x16b.ico"

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "PyTong (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR

  ; Check for installed python
  ReadRegStr $1 HKEY_LOCAL_MACHINE "Software\Classes\Python.NoConFile\shell\open\command" ""
  ; Before: "C:\Python26\pythonw.exe" "%1" %*
  ${WordFind2X} $1 '"' '"' "+1" $2 # C:\Python26\pythonw.exe
  IfFileExists $2 pythonOK ; Path with quotes, according to Leo installed
  # TODO: locate python by hand (file dialog)
  MessageBox MB_OK "Python is not installed. This installed will stop now. Please install Python or associate a program to open *.pyw files."
  Quit
  pythonOK:
  
  ; Put files there
  File /oname=gui.pyw gui.py
  File "tests_dummy.py"
  ; TODO: use an svn export or skip .svn directories
  File /r "avibase_test"
  File /r "icons"
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\PyTong "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyTong" "DisplayName" "PyTong"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyTong" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyTong" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyTong" "NoRepair" 1
  WriteUninstaller "uninstall.exe"
  
SectionEnd

; Optional section (can be disabled by the user)
Section "Start Menu Shortcuts"

  CreateDirectory "$SMPROGRAMS\PyTong"
  CreateShortCut "$SMPROGRAMS\PyTong\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\PyTong\PyTong.lnk" "$INSTDIR\gui.pyw" "" "$INSTDIR\icons\icon32x16b.ico"
  
SectionEnd

;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PyTong"
  DeleteRegKey HKLM SOFTWARE\PyTong

  ; Remove files and uninstaller
  Delete $INSTDIR\gui.py
  Delete $INSTDIR\tests_dummy.py
  RMDir /r "$INSTDIR\icons"
  RMDir /r "$INSTDIR\avibase_test"
  Delete $INSTDIR\uninstall.exe

  ; Remove shortcuts, if any
  Delete "$SMPROGRAMS\PyTong\*.*"

  ; Remove directories used
  RMDir "$SMPROGRAMS\PyTong"
  RMDir "$INSTDIR"

SectionEnd
