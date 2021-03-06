import os
"""
 The shop CSV should hold the initial cash value for the shop.


 Read in customer orders from a CSV file.
– That file should include all the products they wish to buy and in what quantity.


– It should also include their name and their budget.
 The shop must be able to process the orders of the customer.


– Update the cash in the shop based on money received.


* It is important that the state of the shop be consistent.


* You should create customer test files (CSVs) which cannot be completed by the shop e.g. customer wants 400
loaves of bread but the shop only has 20, or the customer wants 2 cans of coke but can only afford 1.
* If these files don’t exist marks penalties will be applied.

– Know whether or not the shop can fill an order.

* Thrown an appropriate error.


 Operate in a live mode, where the user can enter a product by name, specify a quantity, and pay for it. The user should
be able to buy many products in this way.
"""


"""
 The shop CSV should hold the initial cash value for the shop.


 Read in customer orders from a CSV file.
– That file should include all the products they wish to buy and in what quantity.


– It should also include their name and their budget.
 The shop must be able to process the orders of the customer.


– Update the cash in the shop based on money received.


* It is important that the state of the shop be consistent.


* You should create customer test files (CSVs) which cannot be completed by the shop e.g. customer wants 400
loaves of bread but the shop only has 20, or the customer wants 2 cans of coke but can only afford 1.
* If these files don’t exist marks penalties will be applied.

– Know whether or not the shop can fill an order.

* Thrown an appropriate error.


 Operate in a live mode, where the user can enter a product by name, specify a quantity, and pay for it. The user should
be able to buy many products in this way.
"""

from dataclasses import dataclass, field
from typing import List
import csv

@dataclass
class Product:
    name: str
    price: float = 0.0

@dataclass 
class ProductStock:
    product: Product
    quantity: int

@dataclass 
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

def create_and_stock_shop():
    s = Shop()
    with open('../stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        s.cash = float(first_row[0])
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            #print(ps)
    return s


#THIS CODE IS EXECUTED ON STARTUP    
def read_customer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        c = Customer(first_row[0], float(first_row[1]))
        for row in csv_reader:
            name = row[0]
            quantity = float(row[1])
            p = Product(name)
            ps = ProductStock(p, quantity)
            c.shopping_list.append(ps)
        return c 
        

def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')

def print_customer(c):
    print(f'CUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')
    
    for item in c.shopping_list:
        print_product(item.product)
        
        print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity * item.product.price
        print(f'The cost to {c.name} will be €{cost}')
        
def print_shop(s):
    for item in s.stock:
        print_product(item.product)
        print(f'The Shop has {item.quantity} of the above')

s = create_and_stock_shop()


c = read_customer("../customer.csv")
print_customer(c)













def clear_screen(): #this function is used for clearing the screen
    os.system("cls")

def display_menu(): #this funtion is used to display the menu
    print("Chris's Shop")
    print("--------")
    print("MENU")
    print("====")
    print("1 – Customer Menu")
    print("2 - Shop Keeper Menu")
    print("x – Exit application")


def Customer_Menu():
    print("Chris's Shop")
    print("--------")
    print("CUSTOMER MENU")
    print("====")
    print("1 – Load My Orders From CSV")
    print("2 – Buy Products By Name")
    print("x – Exit Menu")

    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
        elif (choice == "x"):
            break;
        else:
            display_menu()


def Shop_Keeper_Menu():
    print("Chris's Shop")
    print("--------")
    print("SHOP KEEPER MENU")
    print("====")
    print("1 – Check shop cash")
    print("2 – Print Shop Stock")
    print("x – Exit Menu")




    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
            print(f'Shop has {s.cash} in cash')
            display_menu()
            
        elif (choice == "2"):
            clear_screen()
            print_shop(s)
        elif (choice == "x"):
            break;
        else:
            display_menu()






# Main function , code was repurposed from lecture menu
def main():
    # Initialise array
    array = []
    display_menu() #This function calls the user menu



    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
            Customer_Menu()
            display_menu()
        elif (choice == "2"):
            clear_screen()
            Shop_Keeper_Menu()
            display_menu()

        elif (choice == "x"):
            break;
        else:
            display_menu()

clear_screen()
if __name__ == "__main__":
    # execute only if run as a script
    main()
