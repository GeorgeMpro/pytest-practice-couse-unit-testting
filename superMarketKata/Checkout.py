class Checkout:
    class Discount:
        def __int__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __int__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(cnt, item)

        return total

    def calculateItemTotal(self, cnt, item):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                nbrOfDiscounts = cnt / discount.nbrItems
                total += nbrOfDiscounts * discount.price
                remaining = cnt % discount.nbrItems
                total += remaining * self.prices[item]
            else:
                total += self.prices[item] * cnt

        else:
            total += self.prices[item] * cnt
        return total

    def addDiscount(self, item, nbrOfItems, price):
        # discount = self.Discount(nbrOfItems, price)
        discount = self.Discount()
        discount.nbrItems = nbrOfItems
        discount.price = price
        self.discounts[item] = discount
