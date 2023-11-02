class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2023"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Dude, item not found in cart.")

    def modify_item(self, item):
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                if item.item_price != 0:
                    self.cart_items[i].item_price = item.item_price
                if item.item_quantity != 0:
                    self.cart_items[i].item_quantity = item.item_quantity
                if item.item_description:
                    self.cart_items[i].item_description = item.item_description
                if item.item_name != "none":
                    self.cart_items[i].item_name = item.item_name
                item_found = True
                break
        if not item_found:
            print("Dude, item not found in cart.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print("Bummer, shopping cart is empty.")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}\n")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        if not self.cart_items:
            print("Bummer, shopping cart is empty.")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
            print("Item Descriptions:")
            for item in self.cart_items:
                print(item.item_name + ": " + item.item_description)


def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("m - Modify item in cart")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        user_choice = input("What's up, dude? Choose an option: ")

        if user_choice == 'a':
            item_name = input("What's the name of the item, dude? ")
            item_description = input("Got a description for it, man? ")
            item_price = float(input("How much does it cost, bro? $"))
            item_quantity = int(input("How many are you getting, my dude? "))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
        elif user_choice == 'r':
            item_name = input("What item are you ditching, bro? ")
            cart.remove_item(item_name)
        elif user_choice == 'm':
            item_name = input("Which item are you changing, dude? ")
            item_price = float(input("What's the new price (enter 0 to keep it the same), man? $"))
            item_quantity = int(input("How many are you getting now, my dude? "))
            item_description = input("Got a new description for it (or leave it blank to keep it the same), my guy? ")
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.modify_item(new_item)
        elif user_choice == 'i':
            cart.print_descriptions()
        elif user_choice == 'o':
            cart.print_total()
        elif user_choice == 'q':
            break
        else:
            print("Whoa, dude, that's not a valid option. Pick something from the menu, man.")


def main():
    customer_name = input("Hey there, bro! What's your name? ")
    current_date = input("What's the date, my dude? ")

    cart = ShoppingCart(customer_name, current_date)

    print("Welcome to the Shopping Cart Program, dude!")
    print_menu(cart)


if __name__ == "__main__":
    main()
