import sqlite3
from tabulate import tabulate
from database import create_db

create_db()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", 
                   (title, author, 1))
    conn.commit()
    conn.close()
    print("Book added successfully!")

def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    print(tabulate(books, headers=["ID", "Title", "Author", "Available"], tablefmt="grid"))

def book_menu():
    while True:
        print("\n=== Book Management ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Go Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")
