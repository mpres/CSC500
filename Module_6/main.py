import ShoppingCart
import os
from IPython.display import clear_output


#Will print a menu to chose a menu fromt
def printMenu():
    print("MENU".center(30))
    print("a - Add item to cart".center(30))
    print("r - Remove item from cart".center(30))
    print("c - Change item quantity".center(30))
    print("i - Output items' descriptions".center(30))
    print("o - Output shopping cart".center(30))
    print("q - Quit".center(30))
    print("Choose an option".center(30))


def main():
  #Instantiate shopping Cart
  customerName = input("Please enter the Customer Name ".center(30))
  dateOfShopping = input("Please enter the Date of the purchase [format: March 6 2024] ".center(30))
  shoppingCart = ShoppingCart.ShoppingCart(customer_name=customerName,current_date = dateOfShopping)
  
  #Initialize first shopping menu
  printMenu()
  userInput = input()
  clear_output(wait=True)
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


    
    printMenu()
    userInput = input()
    clear_output(wait=True)
    os.system('clear')


main()



