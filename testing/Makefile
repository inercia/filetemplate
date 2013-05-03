
PYTHON=python

all: build

bin/buildout:
	$(PYTHON) bootstrap.py

build: bin/buildout
	bin/buildout


clean:
	rm -rf bin build parts temp somefile anotherfile
	rm -rf *.tar.gz *.rpm *.egg-info

distclean: clean
	rm -rf eggs develop-eggs setup.cfg
	
