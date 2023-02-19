install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
lint:
	pylint --disable=R,C ./src ./test

test:
	python -m unittest


all: install lint test