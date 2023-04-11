from library import add_item, modify_item, delete_item

CUSTOMERS_FILE = 'customers.json'


def add_customer(customer):
    add_item(customer, CUSTOMERS_FILE)


def modify_customer(customer_id, customer):
    modify_item(customer_id, customer, CUSTOMERS_FILE)


def delete_customer(customer_id):
    delete_item(customer_id, CUSTOMERS_FILE)
