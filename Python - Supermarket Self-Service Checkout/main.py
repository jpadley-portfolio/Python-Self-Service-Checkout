from CheckoutRegister import CheckoutRegister
from Product import Product
import datetime


def main():
    item_list = []
    #transactions.txt is the output file
    #this line adds to the array and opens the product file
    with open("Product.txt", "rt") as file:
        for each_line in file:
            name, price, barcode = each_line.strip().split(",")
            item_list.append(Product(name, float(price),int(barcode)))

    #Used for starting the scan loop of the program
    while True:
        print("----Welcome to the Self Service Checkout brought to you by ITWorks!----")

        checkout = CheckoutRegister()

    #while loop for scanning
        while True:

            code=int(input("Please scan the barcode of your item! : "))
            found = False

            for item in item_list:
                if item.getBarcode() == code:
                    found = True
                    selected_item = item
                    break
            if found:
                print("{} - ${}".format(selected_item.getName(), selected_item.getPrice()))
                checkout.scan_item(selected_item)
            else:
                print("This item doesn't exist within our inventory. Sorry!")

            #ans = answer
            ans = input("Would you like to scan another item? (Y/N): ").upper()
            print()
            if (ans == "N"):
                break
            elif (ans != "N" and ans != "Y"):
                print ("You have selected the wrong input! Please select either Y or N")

        amount_due = checkout.getTotalPayment()
        #this starts the payment loop for accepting payment
        while True:
            amount = float(input("Payment due: ${0}. Please enter the given amount to pay: ".format(amount_due)))
            if(float(amount) < 0):
                print("Negative money is not a valid currency. You must enter something!")
                continue

            total_payment = checkout.accept_payment(float(amount))
            amount_due -= float(amount)
            if amount_due <= 0:
                break

            #prints receipt
        print("\n")
        print(checkout.print_receipt())

            #this code will write to the Transactions.txt file
        current_date = datetime.datetime.today()
        current_date = current_date.strftime("%d/%m/%y")
        t_list = []
            #read the entered products from the purchased_items
        with open("Transactions.txt", "a") as file:
            for item in checkout.purchased_items:
                    line = checkout.save_transaction(current_date, item.getBarcode(), item.getPrice)
                    file.write(line)
                    file.close()

            next = input("Enter (N) for next or (Q) to not add multiple customers").upper()
            if (next== "Q"):
                break

main()