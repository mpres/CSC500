# Module 6 Portfolio Milestone - 
# Name - Michael Presley
# Date - 12/17/24
# Online Shopping Cart 

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

