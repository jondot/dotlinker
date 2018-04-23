init:
	pipenv install
install:
	pipenv install --dev
env:
	pipenv shell
test:
	pytest
watch:
	ptw
dist:
	rm -rf dist
	rm -rf build
	python setup.py sdist bdist_wheel
dist_install:
	python setup.py install
release:
	twine upload dist/*
.PHONY: init install test dist
