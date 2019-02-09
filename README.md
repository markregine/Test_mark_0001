# test_mark_0001
This is a first attempt to use git and pipy to manage a hypertheticla module i want to build

## I used the following websites to build a module and publish it to pipy.
* #### https://pythonhosted.org/foo-test/minimal.html
* #### https://docs.python.org/3/distutils/setupscript.html
* #### https://packaging.python.org/tutorials/packaging-projects/


## Things learned along the way.
### this statment builds the wheels and eggs
* ### python setup.py sdist bdist_wheel
### documentation says to do this...
* ### python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
### because i have dependencies AND i'm using TestPyPi I need to do this
* ### pip install -i https://testpypi.python.org/pypi --extra-index-url https://pypi.python.org/pypi MODULENAME
### needed to update, but still not working
* ### pip install -i https://testpypi.python.org/pypi --extra-index-url https://pypi.python.org/pypi test_mark_0001 --upgrade
