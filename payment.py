Creditcard_users = [("0217", "Aem", "1111222233334444", "10/11"),("1065", "Aom", "5555666677778888", "11/10")]  #ลิสต์บัตรเครดิตการ์ด
Mobilebank_users = [("0217","Aem","0123401234012"),("1065","Aom","5678956789567")]  #ลิสต์โมบายแบงค์

class PaymentMethod:
    def __init__(self, name):
        self.name = name

    def transaction_id(self, transaction):
        print("Transaction Id : %d" % (transaction))

    def status(self, amount):
        print("Status : Processing payment of $%.2f with %s" % (amount, self.name))

    
class Credit_card:
    def __init__(self, id, name, credit_number, expiration_date):
        self.id = id
        self.name = name
        self.credit_number = credit_number
        self.expiration_date = expiration_date

    def fill_datacredit(self, id, name, credit_number, expiration_date):
        if self.id == id and self.name == name and self.credit_number == credit_number and self.expiration_date == expiration_date:
            return True
        else:
            return False
        
def datacredit():
    id = input("Enter your id: ")
    name = input("Enter your name: ")
    credit_number = input("Enter your credit number: ")
    expiration_date = input("Enter your expiration date: ")
    user = Credit_card(id, name, credit_number, expiration_date)
    if user.fill_datacredit(id, name, credit_number, expiration_date):
        print("Data Complete")
        return
    print("Data Incorrect")

class Mobile_banking:
    def __init__(self, id, name, routing_number):
        self.id = id
        self.name = name
        self.routing_number = routing_number

    def fill_datamobile(self, id, name, routing_number):
        if self.id == id and self.name == name and self.routing_number == routing_number:
            return True
        else:
            return False
def datamobile():
    id = input("Enter your id: ")
    name = input("Enter your name: ")
    routing_number = input("Enter your routing number: ")
    user = Mobile_banking(id, name, routing_number)
    if user.fill_datamobile(id, name, routing_number):
        print("Data Complete")
        return
    print("Data Incorrect")

def main():
    class ChoosePaymentMethod:
        def __init__(self, available_methods):
            self.available_methods = available_methods

        def display_options(self):
            print("Available payment methods:")
            for i, method in enumerate(self.available_methods):
                print("%d. %s" % (i+1, method.name))

        def get_choice(self):
            while True:
                try:
                    choice = int(input("Enter the number of your chosen payment method: "))
                    if choice < 1 or choice > len(self.available_methods):
                        print("Invalid choice. Please enter a number between 1 and %d." % len(self.available_methods))
                    else:
                        return self.available_methods[choice-1]
                except ValueError:
                    print("Invalid choice. Please enter a number between 1 and %d." % len(self.available_methods))

    # PaymentMethod objects
    pm1 = PaymentMethod("Credit Card")
    pm2 = PaymentMethod("Mobile Banking")

    # a ChoosePaymentMethod object
    cpm = ChoosePaymentMethod([pm1, pm2])

    # Display the available options and prompt the user to choose one
    cpm.display_options()
    chosen_method = cpm.get_choice()
    
    if cpm.get_choice() == 1:
        datacredit()
    else:
        datamobile()
        
    # Transaction Id
    transaction = 987654321
    chosen_method.transaction_id(transaction)
    
    # Process the payment using the chosen method
    amount = 50.00  # for example
    chosen_method.status(amount)

if __name__ == "__main__":
    main()
