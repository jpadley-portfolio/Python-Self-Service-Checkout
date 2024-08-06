#Product class
class Product():


    #product constructor
    def __init__(self, name, price, barcode):
        self.name = name
        self.price = price
        self.barcode = barcode

    #getters for Barcode, Name & Price
    def getBarcode(self):
        return self.barcode

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price