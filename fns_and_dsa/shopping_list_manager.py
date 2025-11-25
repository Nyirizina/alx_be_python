def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. add item")
    print("2. remove item")
    print("3. view list")
    print("4. exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("choose your option:")
        if choice == '1':
            item = input("add to cart:")
            shopping_list.append(item)
            print(f"{item} added to cart.")
        elif choice == '2':
            item = input("remove from cart:")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from cart.")
            else:
                print(f"{item} not found in cart.")
        elif choice == '3':
            print("shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == '4':
            print("exiting thanks for passing by .....")
            break
        else:
            print("invalid option please try again.")
if __name__ == "__main__":
    main()