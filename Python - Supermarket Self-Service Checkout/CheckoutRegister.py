import Product
import datetime


# code that sets up the CheckoutRegister class
class CheckoutRegister:
    def __init__(self):
        self.total_payment=0.0
        self.received_amount=0.0
        self.purchased_items=[]

    # getter for total payment
    def getTotalPayment(self):
        return self.total_payment

    #method used to accept payment
    def accept_payment(self, giveAmount):
        self.received_amount+=giveAmount
        return self.received_amount

    #method used for scanning items
    def scan_item(self, scanProduct):
        self.total_payment+=scanProduct.getPrice()
        self.purchased_items.append(scanProduct)

    #method used for printing receipt
    def print_receipt(self):
        receipt = "---Final Receipt---"
        receipt += "\n"
        for p in self.purchased_items:
            receipt += p.getName() + " " + "$" +str(p.getPrice()) + "\n"
        receipt += "\n"
        receipt += "Total Amount due: $" + str(self.total_payment) + "\n"
        receipt += "Amount received: $" + str(self.received_amount) + "\n"
        receipt += "Total change given: $" + str(self.received_amount - self.total_payment) + "\n"
        receipt += "Thank you from ITWorks for shopping at our store!\n"
        return receipt

    def save_transaction(self, current_date, barcode, amount):
        message = str(current_date) + "" + str(barcode) + "" + str(amount) + "\n"
        return message
