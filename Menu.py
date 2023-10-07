#Get the first item
print("Item 1")
item1_name = input("Enter the item name:\n")
item1_price = float(input("Enter the item price:\n"))
item1_quantity = int(input("Enter the item quantity:\n"))

#Get the second item
print("\nItem 2")
item2_name = input("Enter the item name:\n")
item2_price = float(input("Enter the item price:\n"))
item2_quantity = int(input("Enter the item quantity:\n"))

#Calculate the cost
item1_cost = item1_price * item1_quantity
item2_cost = item2_price * item2_quantity
total_cost = item1_cost + item2_cost

#Print it out
print("\nTOTAL COST")
print(f"{item1_name} {item1_quantity} @ ${item1_price:.2f} = ${item1_cost:.2f}")
print(f"{item2_name} {item2_quantity} @ ${item2_price:.2f} = ${item2_cost:.2f}")
print(f"Total: ${total_cost:.2f}")
