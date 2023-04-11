import datetime
from library import add_item, modify_item, delete_item, load_data, save_data
import borrowings

BLACKLIST_FILE = 'blacklist.json'


def update_blacklist():
    customers = load_data('customers.json')
    borrowings_list = borrowings.load_data(borrowings.BORROWINGS_FILE)
    blacklist = load_data(BLACKLIST_FILE)

    for customer in customers:
        customer_id = customer['id']
        borrowed_items = borrowings.get_borrowed_items(customer_id)
        overdue_items = [item for item in borrowed_items if is_overdue(item)]

        if overdue_items and customer_id not in [entry['customer_id'] for entry in blacklist]:
            blacklist_entry = {
                'customer_id': customer_id,
                'penalty_count': len(overdue_items),
                'blacklisted_since': datetime.date.today().isoformat()
            }
            add_item(blacklist_entry, BLACKLIST_FILE)
        elif not overdue_items and customer_id in [entry['customer_id'] for entry in blacklist]:
            delete_blacklist_entry(customer_id)


def is_overdue(borrowing):
    due_date = datetime.date.fromisoformat(borrowing['due_date'])
    return datetime.date.today() > due_date


def delete_blacklist_entry(customer_id):
    blacklist = load_data(BLACKLIST_FILE)
    index = next((i for i, entry in enumerate(blacklist)
                 if entry['customer_id'] == customer_id), None)
    if index is not None:
        del blacklist[index]
        save_data(blacklist, BLACKLIST_FILE)


def is_blacklisted(customer_id):
    blacklist = load_data(BLACKLIST_FILE)
    return any(entry['customer_id'] == customer_id for entry in blacklist)


def get_blacklist():
    return load_data(BLACKLIST_FILE)
