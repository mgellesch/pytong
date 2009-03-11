RESOURCES="../dist/PyTong.app/Contents/Resources"

all: dmg

clean:
	rm -fr ../dist/PyTong.app
	rm ../dist/*.dmg
	
dmg: app
	hdiutil create ../dist/PyTong-0.1.dmg -volname "PyTong-0.1" -fs HFS+ -srcfolder "../dist/PyTong.app"

app: clean
	svn export PyTong.app ../dist/PyTong.app
	cp ../*.py ${RESOURCES}
	svn export ../icons ${RESOURCES}/icons
	svn export ../avibase_test ${RESOURCES}/avibase_test
