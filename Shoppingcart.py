def display_cart(cart):
    if not cart:
        print('Cart is empty')
    else:
        print("Shopping Cart: ")

    total_price =0
    for item in cart:
        print(f"{item['name']}: ${item['price']}")
        total_price += item['price']
    print(f"Total: ${total_price:.2f}")
def main():
    cart =[]
    while True:
        print("\nShopping Cart Application")
        print("1.Add Item to Cart")
        print("2.View Cart")
        print("3.Remove item from Cart")
        print("4.Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter Item name: ")
            item_price = float(input("Enter Item price: "))
            item = {'name':item_name,'price':item_price}
            cart.append(item)
            print("Item added to cart!")
        elif choice == '2':
            display_cart(cart)
        elif choice == '3':
            if not cart:
                print("Your Cart is already empty")
            else:
                display_cart(cart)
                item_index = int(input("Enter the item number to remove: ")) -1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"Removed item: {removed_item['name']}")
                else:
                    print("Invalid item number.")
        elif choice == '4':
            print("Exit the application")
            break
        else:
            print("Invalid choice. Please select a valid option")

if __name__ == "__main__":
    main()