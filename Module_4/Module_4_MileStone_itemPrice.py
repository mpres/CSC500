#Michael Presley 12/3/24 Module 4 Portfolio Milestone
#Make Item to Purchase class
class ItemToPurchase:
  def __init__ (self,item_name="none",item_price = 0.0,item_quantity = 0):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity

  def print_item_cost(self):
    total = self.item_price * self.item_quantity
    return(f"The total cost of item {self.item_name}, is ${total}")
    


#Step 2

print("Item 1")
item_name_1 = input("Please enter item name ")
item_price_1 = float(input("Please the enter item price "))
item_qty_1 = int(input("Please the enter item quantity "))

print("Item 2")
item_name_2 = input("Please enter item name ")
item_price_2 = float(input("Please the enter item price "))
item_qty_2 = int(input("Please the enter item quantity "))


item1 = ItemToPurchase(item_name=item_name_1,item_price=item_price_1,item_quantity=item_qty_1)
item2 = ItemToPurchase(item_name=item_name_2,item_price=item_price_2,item_quantity=item_qty_2)

#Step 3 

#Calculate the  total cost

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity) 

print("TOTAL COST")

print(f"{item1.item_name} {item1.item_quantity} @ ${item1.item_price} = ${item1.item_price * item1.item_quantity}" )
print(f"{item2.item_name} {item2.item_quantity} @ ${item2.item_price} = ${item2.item_price * item2.item_quantity}" )

print(f"Total: ${total_cost}")


