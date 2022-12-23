from pytest import approx, raises


def test_assert():
    # more accurate for floating point values 1-e6 or something
    assert (0.1 + 0.2) == approx(0.3)


def raisesValueException():
    raise ValueError


def test_exception():
    with raises(ValueError):
        raisesValueException()
