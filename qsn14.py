products = {}

while True:
    print("\nMenu:")
    print("1. Add a new product")
    print("2. Update price of an existing product")
    print("3. View all products")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter product name: ").strip()
        if name in products:
            print("Product already exists.")
        else:
            try:
                price = float(input("Enter product price: "))
                products[name] = price
                print(f"Product '{name}' added with price {price}")
            except ValueError:
                print("Invalid price. Please enter a number.")

    elif choice == "2":
        name = input("Enter product name to update: ").strip()
        if name in products:
            try:
                new_price = float(input("Enter new price: "))
                products[name] = new_price
                print(f"Price of '{name}' updated to {new_price}")
            except ValueError:
                print("Invalid price. Please enter a number.")
        else:
            print("Product not found.")

    elif choice == "3":
        if not products:
            print("No products available.")
        else:
            print("\nProduct List:")
            for name, price in products.items():
                print(f"{name}: {price}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
