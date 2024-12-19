# Module 6 Portfolio Milestone -
# Name - Michael Presley
# Date - 12/17/24
# Online Shopping Cart

import os
from IPython.display import clear_output


#Let's create the Shopping Cart Class
class ShoppingCart:
  def  __init__ (self, customer_name: str, current_date: str, cart_items: list = []):
    self.customer_name = customer_name
    self.current_date = current_date
    self.title = customer_name + "'s Shopping Cart - " + current_date
    self.cart_items = cart_items

  def add_item(self, ItemToPurchase: dict = {"description":"","quantity":0,"price":0.00}):
    self.cart_items.append(ItemToPurchase)

  def remove_item(self, itemName):
    if itemName not in [item['name'] for item in self.cart_items]:
      print(f"{itemName} not found in cart. Nothing removed.")
    else:
      item = next(item for item in self.cart_items if item['name'] == itemName)
      self.cart_items.remove(item)

  def modify_item(self, ItemToPurchase: dict):
    #look for item in cart
    #self.ItemToPurchcase = ItemToPurchase
    for a in self.cart_items:
      if a['name'] == ItemToPurchase['name']:
        if ItemToPurchase['quantity'] > 0:
          a['quantity'] = ItemToPurchase['quantity']
        if ItemToPurchase['price'] > 0.00:
          a['price'] = ItemToPurchase['price']
        if ItemToPurchase['description'] != "":
          a['description'] = ItemToPurchase['description']
      else:
        print(f"{ItemToPurchase['name']} not found in cart. Nothing modified.")

  def get_num_items_in_cart(self):
    return sum([x['quantity'] for x in self.cart_items])

  def get_cost_of_cart(self):
    return sum([x['quantity'] * x['price'] for x in self.cart_items])

  def print_total(self):
    if self.cart_items == []:
      print("SHOPPING CART IS EMPTY")
    else:
      print(self.title)
      #for item in self.cart_tie
      number_of_items = self.get_num_items_in_cart()
      print(f"Number of Items: {number_of_items}")
      #print each individual item out
      for item in self.cart_items:
        print(f"{item['name']} {item['quantity']} @ ${item['price']:.2f} = ${(item['price']*item['quantity']):.2f}")
      total = sum([x['quantity'] * x['price'] for x in self.cart_items])
      print(f"Total: ${total:.2f}")

  def print_descriptions(self):
    if self.cart_items == []:
      print("SHOPPING CART IS EMPTY")
    else:
      print(self.title)
      print("Item Descriptions")
      for item in self.cart_items:
        print(f"{item['name']}: {item['description']}")




#Will print a menu to chose a menu fromt
def print_menu():
    print("MENU".center(30))
    print("a - Add item to cart".center(30))
    print("r - Remove item from cart".center(30))
    print("c - Change item quantity".center(30))
    print("i - Output items' descriptions".center(30))
    print("o - Output shopping cart".center(30))
    print("q - Quit".center(30))
    print("Choose an option".center(30))




#Let's define the main function that will run the program
def main():
  #Instantiate shopping Cart
  customerName = input("Please enter the Customer Name ".center(30))
  dateOfShopping = input("Please enter the Date of the purchase [format: March 6 2024] ".center(30))
  shoppingCart = ShoppingCart(customer_name=customerName,current_date = dateOfShopping)

  #Initialize first shopping menu
  print_menu()
  userInput = input()
  os.system('clear')


  #print(userInput)
  while userInput != 'q':
    if userInput == 'q':
      print("Thank you for shopping with us")
      break
    elif userInput == 'a':
      itemName = input("Please enter the name of the new item ")
      description = input("Please enter the description for the new item ")
      quantity = int(input("Please enter the quantity of the items purchased "))
      price = float(input("Please enter the price for the new item "))
      item_dict = {"name":itemName,"description":description, "price":price,"quantity":quantity}

      shoppingCart.add_item(item_dict)
    elif userInput == 'r':
      removeItemName = input("Enter the name of the item you would like to remove ")
      shoppingCart.remove_item(removeItemName)
    elif userInput == 'c':
      #change the quantity of the item

      modifyItemName = input("Enter the name of the item you would like to change the quantity ")
      modifyQty = int(input("Please enter the new quantity"))

      modifyDict = {"name":modifyItemName, 'quantity':modifyQty, 'description':"", 'price':0.00}

      shoppingCart.modify_item(modifyDict)

    elif userInput == 'i':
      # output item descriptions
      shoppingCart.print_descriptions()

    elif userInput == 'o':
      shoppingCart.print_total()
    else:
      print(f"Sorry, the input {userInput} is not a valid option")



    print_menu()
    userInput = input()
    
    os.system('clear')


# Run Program
main()



