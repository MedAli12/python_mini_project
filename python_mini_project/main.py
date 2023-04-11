import matplotlib.pyplot as plt
import datetime
from books import add_book, modify_book, delete_book, search_books
from customers import add_customer, modify_customer, delete_customer
from subscriptions import add_subscription, renew_subscription, is_subscription_active
from borrowings import borrow_item, return_item, get_borrowed_items, get_borrowing_history
from blacklist import update_blacklist, is_blacklisted, get_blacklist
from accounting import add_expense, display_monthly_expenses_curve, get_monthly_income


def main_menu():
    print("Welcome to the Library Management System!")
    print("Please choose an option:")
    print("1. Books management")
    print("2. Customers management")
    print("3. Subscriptions management")
    print("4. Borrowings management")
    print("5. Blacklist management")
    print("6. Accounting management")
    print("0. Exit")


def books_menu():
    print("Books management:")
    print("1. Add book")
    print("2. Modify book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Back to main menu")


def customers_menu():
    print("Customers management:")
    print("1. Add customer")
    print("2. Modify customer")
    print("3. Delete customer")
    print("0. Back to main menu")


def subscriptions_menu():
    print("Subscriptions management:")
    print("1. Create subscription")
    print("2. Renew subscription")
    print("0. Back to main menu")


def borrowings_menu():
    print("Borrowings management:")
    print("1. Borrow item")
    print("2. Return item")
    print("3. Get borrowed items")
    print("4. Get borrowing history")
    print("0. Back to main menu")


def blacklist_menu():
    print("Blacklist management:")
    print("1. Update blacklist")
    print("2. Get blacklist")
    print("0. Back to main menu")


def accounting_menu():
    print("Accounting management:")
    print("1. Add expense")
    print("2. Display monthly expenses curve")
    print("0. Back to main menu")


def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            books_management()
        elif choice == '2':
            customers_management()
        elif choice == '3':
            subscriptions_management()
        elif choice == '4':
            borrowings_management()
        elif choice == '5':
            blacklist_management()
        elif choice == '6':
            accounting_management()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


def books_management():
    while True:
        books_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add book
            id = int(input("Enter the book ID : "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book publication year: "))
            ISBN = input("Enter book ISBN: ")
            description = input("Enter book description: ")
            category = input("Enter book category: ")
            number_of_copies = int(input("Enter number of copies: "))
            page_number = int(input("Enter number of pages: "))
            publisher = input("Enter book publisher: ")

            book = {
                'id': id,
                'title': title,
                'author': author,
                'year': year,
                'ISBN': ISBN,
                'description': description,
                'category': category,
                'number_of_copies': number_of_copies,
                'page_number': page_number,
                'publisher': publisher
            }
            add_book(book)
            print("Book added successfully.")
        elif choice == '2':
            # Modify book
            book_id = int(input("Enter the book ID to modify: "))
            print("Enter new values (leave blank to keep the current value):")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new publication year: ")
            ISBN = input("Enter new ISBN: ")
            description = input("Enter new description: ")
            category = input("Enter new category: ")
            number_of_copies = input("Enter new number of copies: ")
            page_number = input("Enter new number of pages: ")
            publisher = input("Enter new publisher: ")

            updated_book = {}
            if title:
                updated_book['title'] = title
            if author:
                updated_book['author'] = author
            if year:
                updated_book['year'] = int(year)
            if ISBN:
                updated_book['ISBN'] = ISBN
            if description:
                updated_book['description'] = description
            if category:
                updated_book['category'] = category
            if number_of_copies:
                updated_book['number_of_copies'] = int(number_of_copies)
            if page_number:
                updated_book['page_number'] = int(page_number)
            if publisher:
                updated_book['publisher'] = publisher

            modify_book(book_id, updated_book)
            print("Book modified successfully.")
        elif choice == '3':
            # Delete book
            book_id = int(input("Enter the book ID to delete: "))
            delete_book(book_id)
            print("Book deleted successfully.")
        elif choice == '4':
            # Search books
            print("Enter search criteria (leave blank to skip):")
            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            year = input("Enter publication year: ")

            criteria = {}
            if title:
                criteria['title'] = title
            if author:
                criteria['author'] = author
            if category:
                criteria['category'] = category
            if year:
                criteria['year'] = int(year)

            books = search_books(criteria)
            print(f"Books found: {books}")
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


def customers_management():
    while True:
        customers_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add customer
            id = int(input("Enter customer ID: "))
            surname = input("Enter customer surname: ")
            first_name = input("Enter customer first name: ")
            cin = input("Enter customer CIN: ")
            gender = input("Enter customer gender (male/female): ")
            date_of_birth = input(
                "Enter customer date of birth (YYYY-MM-DD): ")
            address = input("Enter customer address: ")
            telephone_number = input("Enter customer telephone number: ")

            customer = {
                'id': id,
                'surname': surname,
                'first_name': first_name,
                'cin': cin,
                'gender': gender,
                'date_of_birth': date_of_birth,
                'address': address,
                'telephone_number': telephone_number
            }
            add_customer(customer)
            print("Customer added successfully.")
        elif choice == '2':
            # Modify customer
            customer_id = int(input("Enter the customer ID to modify: "))
            print("Enter new values (leave blank to keep the current value):")
            surname = input("Enter new surname: ")
            first_name = input("Enter new first name: ")
            cin = input("Enter new CIN: ")
            gender = input("Enter new gender (male/female): ")
            date_of_birth = input("Enter new date of birth (YYYY-MM-DD): ")
            address = input("Enter new address: ")
            telephone_number = input("Enter new telephone number: ")

            updated_customer = {}
            if surname:
                updated_customer['surname'] = surname
            if first_name:
                updated_customer['first_name'] = first_name
            if cin:
                updated_customer['cin'] = cin
            if gender:
                updated_customer['gender'] = gender
            if date_of_birth:
                updated_customer['date_of_birth'] = date_of_birth
            if address:
                updated_customer['address'] = address
            if telephone_number:
                updated_customer['telephone_number'] = telephone_number

            modify_customer(customer_id, updated_customer)
            print("Customer modified successfully.")
        elif choice == '3':
            # Delete customer
            customer_id = int(input("Enter the customer ID to delete: "))
            delete_customer(customer_id)
            print("Customer deleted successfully.")
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


def subscriptions_management():
    while True:
        subscriptions_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Create subscription
            customer_id = int(
                input("Enter the customer ID for the subscription: "))
            add_subscription(customer_id)
            print("Subscription created successfully.")
        elif choice == '2':
            # Renew subscription
            customer_id = int(
                input("Enter the customer ID for the subscription renewal: "))
            renew_subscription(customer_id)
            print("Subscription renewed successfully.")
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


def borrowings_management():
    while True:
        borrowings_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Borrow item
            customer_id = int(input("Enter the customer ID: "))
            item_id = int(input("Enter the item ID to borrow: "))
            borrow_item(customer_id, item_id)
            print("Item borrowed successfully.")
        elif choice == '2':
            # Return item
            customer_id = int(input("Enter the customer ID: "))
            item_id = int(input("Enter the item ID to return: "))
            return_item(customer_id, item_id)
            print("Item returned successfully.")
        elif choice == '3':
            # Get borrowed items
            customer_id = int(input("Enter the customer ID: "))
            borrowed_items = get_borrowed_items(customer_id)
            print(
                f"Borrowed items for customer {customer_id}: {borrowed_items}")
        elif choice == '4':
            # Get borrowing history
            customer_id = int(input("Enter the customer ID: "))
            history = get_borrowing_history(customer_id)
            print(f"Borrowing history for customer {customer_id}: {history}")
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


def blacklist_management():
    while True:
        blacklist_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Update blacklist
            update_blacklist()
            print("Blacklist updated successfully.")
        elif choice == '2':
            # Get blacklist
            blacklist = get_blacklist()
            print(f"Blacklisted customers: {blacklist}")
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


def accounting_management():
    while True:
        accounting_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Get monthly income
            income_data = get_monthly_income()
            print(f"Monthly income: {income_data}")

            months = list(income_data.keys())
            income = list(income_data.values())

            plt.plot(months, income, marker='o')
            plt.xlabel('Months')
            plt.ylabel('Income (Tunisian Dinar)')
            plt.title('Monthly Income')
            plt.grid()
            plt.show()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
