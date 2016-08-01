all: clean
	@pip install -r requirements.txt
	@flask initdb
	@flask run --host=0.0.0.0
	

clean:
	@find . -name "*.pyc" -delete
	@find . -name '*__pycache__' -delete
	@find . -name ".coverage" -delete


tests: clean
	
	@nosetests --rednose --exe --with-coverage --cover-package application -v
	@pycodestyle .
