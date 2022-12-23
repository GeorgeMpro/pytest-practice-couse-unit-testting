import pytest


@pytest.fixture(scope="session", autouse=True)
def setup():
    print("\nSetup session")


@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module")


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup function")


def test1(setup):
    print("Executing test1!")
    assert True


@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2!")
    assert True
