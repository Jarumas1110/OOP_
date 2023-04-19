#from datetime import datetime
#from copy import deepcopy
#from fastapi import FastAPI

#app = FastAPI()

class Product:
    def __init__(self,name,stock,full_price,pro_price,color):
        self.name = name
        self.stock = stock
        self.full_price = full_price
        self.pro_price = pro_price #promotion price
        self.color = color

class Item(Product):
    def __init__(self,name,stock,full_price,pro_price,color):
        super().__init__(name,stock,full_price,pro_price,color)
        #self.quantity = quantity 

class Address:
    def __init__(self,name,phone,house_address,sub_district,district,province,postcode):
        self.name = name
        self.phone = phone
        self.house_address = house_address
        self.sub_district = sub_district
        self.district = district
        self.province = province
        self.postcode = postcode

addr = []

def create_addresss():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    house_address = input("Enter house-address: ")
    sub_district = input("Enter sub-district: ")
    district = input("Enter district: ")
    province = input("Enter province: ")
    postcode = input("Enter postcode: ")
    address = Address(name,phone,house_address,sub_district,district,province,postcode)
    addr.append(address)
    return addr


class Shipping:
    def __init__(self, shipping_name, cost):
        self.shipping_name = shipping_name
        self.cost = cost

    def calculate_cost(self):
        return self.cost

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            else:
                del self.items[item]

    def clear(self):
        self.items = {}

class Order:
    def __init__(self, cart, shipping):
        self.cart = cart
        self.shipping = shipping
        self.payment = None
    def total_price(self): #เป็นราคารวมของสินค้าที่ลดแล้ว
        total_price = sum([item.pro_price * quantity for item, quantity in self.cart.items.items()])
        return total_price
    #def discount(self):
    #    discount = sum([(item.full_price - item.pro_price) * quantity for item, quantity in self.cart.items.items()])
    #    return discount
    def net_balance(self):
        shipping_cost = self.shipping.calculate_cost()
        net_balance = sum([item.pro_price * quantity for item, quantity in self.cart.items.items()]) + shipping_cost
        return net_balance

    #def calculate_total(self): # ราคาแบบ netbalance
    #    total_price = sum([item.full_price * quantity for item, quantity in self.cart.items.items()])
    #    discount = sum([(item.full_price - item.pro_price) * quantity for item, quantity in self.cart.items.items()])
    #    shipping_cost = self.shipping.calculate_cost()
    #    net_balance = total_price - discount + shipping_cost
    #    return net_balance

    
    def place(self):
        print("Order :")
        for item, quantity in self.cart.items.items():
            print("%s x %d %d Baht" % (item.name, quantity,item.pro_price))
        print("Total Price: %.2f Baht" % self.total_price())
        #print("Discount: %.2f Baht" % self.discount())
        print("Shipping cost: %.2f Baht" % self.shipping.calculate_cost())
        print("Net Balance: %.2f Baht" % self.net_balance())


def main():
    # Create some products
    lipstick = Item("Oh My Matte",1000,259,129,"OMM07")
    blush = Item("Oh My Blush",1250,299,149,"02Milkshake")

    # Create a shipping method
    sp1 = Shipping("Kerry", 65.00)
    sp2 = Shipping("EMS", 50.00)
#------------------------------------------------------------------------------------------#
    # Create a cart and add items
    cart = Cart()
    cart.add_item(lipstick, 2)
    cart.add_item(blush)
    # Choose Shipping
#    choice = input("Choose your shipping : ")
#    if choice == 1:
#       Shipping.calculate_cost = sp1.cost
#    elif choice == 2 :
#        Shipping.calculate_cost = sp2.cost
    # Create an order

    order = Order(cart, sp1)

   
    # Place the order
    order.place()
    create_addresss()
    # Clear the cart
    cart.clear()
    print("\n")
#------------------------------------------------------------------------------------------#
    # Add items to the cart
    cart.add_item(lipstick, 2)
    cart.add_item(blush, 4)
    cart.remove_item(blush)

    # Create a different order
    order2 = Order(cart, sp2)

    # Place the order
    order2.place()
    create_addresss()
    # Clear the cart
    cart.clear()
    print("\n")

if __name__ == "__main__":
    main()