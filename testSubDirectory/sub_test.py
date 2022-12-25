# run the tests in the directory
# pytest -v -s testSubDirectory/
import pytest


# run just the files
# pytest -v -s assert_exception_test.py

# run only with the given keyword
#  pytest -v -s -k "test2"
# running more using the or keyword
#  pytest -v -s -k "test2 or test3"

# run marked tests, can also use the "or" keyword
# pytest -v -s -m test12

def test3():
    print("\ntest3")
    assert True


@pytest.mark.test12
def test12():
    print("\ntest12")
    assert True
