init:
		pip install -r requirements.txt

init_test:
		pip install -r test_requirements.txt

test:
		nosetests tests
