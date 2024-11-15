from book_manager import book_menu
from member_manager import member_menu

def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_menu()
        elif choice == "2":
            member_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
