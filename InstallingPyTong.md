# System Requirements #

  * [Python](http://www.python.org)
  * [wxPython](http://www.wxpython.org)
> > try 'import wx' from the Python interpreter to see if wx is installed.

## Windows ##

The Downloads page contains an installer for Windows. It will install into `C:\Program Files` by default, and add a PyTong entry to the Start Menu.
The installer checks the registry for whichever application is set up to handle .pyw files (windowed Python programs) and uses it to launch PyTong.

## OS X ##

The Downloads page contains a disk image for OS X. It contains a ready to run application bundle which you can drag to `/Applications` or anywhere else. Recent versions of OS X have Python and wxPython installed by default. If you have installed a newer Python yourself, install wxPython as well (try 'import wx' from the interpreter to check for wx).

## Linux / other ##

Right now there is no source distribution yet, but you can checkout the latest version with Subversion. To run PyTong, run the script `gui.py`.

Example:
```
svn checkout http://pytong.googlecode.com/svn/trunk/ pytong
cd pytong
python gui.py
```