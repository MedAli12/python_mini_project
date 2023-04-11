import datetime
from library import add_item, modify_item, delete_item, load_data, save_data
import subscriptions

BORROWINGS_FILE = 'borrowings.json'


def borrow_item(customer_id, item_id, due_date=None, premium=False):
    if subscriptions.is_subscription_active(customer_id):
        if can_borrow(customer_id, premium):
            if not due_date:
                due_date = datetime.date.today() + datetime.timedelta(weeks=2)
            borrowing = {
                'customer_id': customer_id,
                'item_id': item_id,
                'borrow_date': datetime.date.today().isoformat(),
                'due_date': due_date.isoformat()
            }
            add_item(borrowing, BORROWINGS_FILE)
        else:
            raise ValueError("Customer has reached the borrowing limit")
    else:
        raise ValueError("Customer subscription is not active")


def can_borrow(customer_id, premium):
    borrowings = load_data(BORROWINGS_FILE)
    borrowed_items = [borrowing for borrowing in borrowings if borrowing['customer_id']
                      == customer_id and not borrowing.get('return_date')]
    limit = 5 if premium else 3
    return len(borrowed_items) < limit


def return_item(customer_id, item_id):
    borrowings = load_data(BORROWINGS_FILE)
    for borrowing in borrowings:
        if borrowing['customer_id'] == customer_id and borrowing['item_id'] == item_id and not borrowing.get('return_date'):
            borrowing['return_date'] = datetime.date.today().isoformat()
            save_data(borrowings, BORROWINGS_FILE)
            break
    else:
        raise ValueError("Item not found in customer borrowings")


def get_borrowed_items(customer_id):
    borrowings = load_data(BORROWINGS_FILE)
    return [borrowing for borrowing in borrowings if borrowing['customer_id'] == customer_id and not borrowing.get('return_date')]


def get_borrowing_history(customer_id):
    borrowings = load_data(BORROWINGS_FILE)
    return [borrowing for borrowing in borrowings if borrowing['customer_id'] == customer_id]
