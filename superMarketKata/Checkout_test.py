import pytest

from superMarketKata.Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    # allows to access the def __int__ variables inside the checkout object(?)
    checkout.__int__()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)

    return checkout


def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3


# skip test
# @pytest.mark.skip
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")

    assert checkout.calculateTotal() == 2


def test_canApplyDiscountRule2(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addDiscount("b", 4, 2)
    checkout.addItem("b")
    checkout.addItem("b")
    checkout.addItem("b")
    checkout.addItem("b")

    assert checkout.calculateTotal() == 4