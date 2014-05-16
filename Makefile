#OSX 
OPEN = open
#LINUX
#OPEN = xdg-open
#WINDOWS
#OPEN = start 

coverage:
	nosetests --with-coverage --cover-package=weather --cover-html
	$(OPEN) cover/index.html 
test:
	nosetests 