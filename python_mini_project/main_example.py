import datetime
from books import add_book, modify_book, delete_book
from customers import add_customer, modify_customer, delete_customer
from subscriptions import add_subscription, renew_subscription, is_subscription_active
from borrowings import borrow_item, return_item, get_borrowed_items, get_borrowing_history
from blacklist import update_blacklist, is_blacklisted, get_blacklist
from accounting import add_expense, display_monthly_expenses_curve


def main():
    # Add books
    book1 = {
        'id': 1,
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'year': 1951,
        'ISBN': '0316769487',
        'description': 'A story about teenage rebellion',
        'category': 'fiction',
        'number_of_copies': 3,
        'page_number': 277,
        'publisher': 'Little, Brown and Company'
    }
    add_book(book1)

    # Add customers
    customer1 = {
        'id': 1,
        'surname': 'Smith',
        'first_name': 'John',
        'cin': '12345678',
        'gender': 'male',
        'date_of_birth': '1990-01-01',
        'address': '123 Main St',
        'telephone_number': '555-1234'
    }
    add_customer(customer1)

    # Create subscription
    add_subscription(customer1['id'])

    # Borrow item
    borrow_item(customer1['id'], book1['id'])

    # Display borrowed items
    print(
        f"Borrowed items for customer {customer1['id']}: {get_borrowed_items(customer1['id'])}")

    # Update and display blacklist
    update_blacklist()
    print(f"Blacklist: {get_blacklist()}")

    # Return item
    return_item(customer1['id'], book1['id'])

    # Display borrowing history
    print(
        f"Borrowing history for customer {customer1['id']}: {get_borrowing_history(customer1['id'])}")

    # Add expense
    add_expense(datetime.date.today(), 15)

    # Display monthly expenses curve
    display_monthly_expenses_curve()


if __name__ == "__main__":
    main()
