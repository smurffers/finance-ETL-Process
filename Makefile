install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
lint:
	pylint --disable=R,C *.py devopslib

test:
	python -m unittest


all: install lint test format 