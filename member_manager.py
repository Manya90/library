import sqlite3
from tabulate import tabulate
from database import create_db

create_db()

def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Member added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    conn.close()

def view_members():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    conn.close()
    print(tabulate(members, headers=["ID", "Name", "Email"], tablefmt="grid"))

def member_menu():
    while True:
        print("\n=== Member Management ===")
        print("1. Add Member")
        print("2. View All Members")
        print("3. Go Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")
