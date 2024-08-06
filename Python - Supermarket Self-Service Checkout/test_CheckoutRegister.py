import unittest
from CheckoutRegister import CheckoutRegister
from Product import Product

#testing for the Product class
class test_Product(unittest.TestCase):
    testProduct = Product("Coke", 2.50, 101)

    def testGetBarcode(self):
        barcode = self.testProduct.getBarcode()
        self.assertEqual(102, barcode)

    def testGetName(self):
        name = self.testProduct.getName()
        self.assertEqual("Coke", name)

    def testGetPrice(self):
        price = self.testProduct.getPrice()
        self.assertEqual(2.50, price)


    #testing for the checkout
class test_Checkout(unittest.TestCase):

    def test_scan_item(self):
        checkout = CheckoutRegister()
        item = Product(101, "Coke", 2.50)
        checkout.purchased_items.append(item)
        self.assertEqual(checkout.scan_item(item),None)

    def test_accept_payment(self):
        checkout = CheckoutRegister()
        amount = 10
        checkout.accept_payment(amount)
        self.assertEqual(checkout.received_amount, amount)

    def test_init(self):
        checkout = CheckoutRegister()
        self.assertEqual(len(checkout.purchased_items), 0)
        self.assertEqual(checkout.total_payment, 0)
        self.assertEqual(checkout.received_amount, 0)


if __name__ == "__main__":
    unittest.main()