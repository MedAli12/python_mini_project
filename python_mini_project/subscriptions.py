import datetime
from library import add_item, modify_item, delete_item, load_data, save_data

SUBSCRIPTIONS_FILE = 'subscriptions.json'


def add_subscription(customer_id, start_date=None, duration_in_months=1):
    if not start_date:
        start_date = datetime.date.today()
    end_date = calculate_end_date(start_date, duration_in_months)
    subscription = {
        'customer_id': customer_id,
        'start_date': start_date.isoformat(),
        'end_date': end_date.isoformat()
    }
    add_item(subscription, SUBSCRIPTIONS_FILE)


def calculate_end_date(start_date, duration_in_months):
    end_year = start_date.year + \
        (start_date.month + duration_in_months - 1) // 12
    end_month = (start_date.month + duration_in_months - 1) % 12 + 1
    end_day = start_date.day
    return datetime.date(end_year, end_month, end_day)


def renew_subscription(customer_id, duration_in_months=1):
    subscriptions = load_data(SUBSCRIPTIONS_FILE)
    for subscription in subscriptions:
        if subscription['customer_id'] == customer_id:
            start_date = datetime.date.fromisoformat(subscription['end_date'])
            end_date = calculate_end_date(start_date, duration_in_months)
            subscription['start_date'] = start_date.isoformat()
            subscription['end_date'] = end_date.isoformat()
            save_data(subscriptions, SUBSCRIPTIONS_FILE)
            break
    else:
        raise ValueError("Subscription not found")


def is_subscription_active(customer_id):
    subscriptions = load_data(SUBSCRIPTIONS_FILE)
    for subscription in subscriptions:
        if subscription['customer_id'] == customer_id:
            end_date = datetime.date.fromisoformat(subscription['end_date'])
            return datetime.date.today() <= end_date
    return False


def get_subscription(customer_id):
    subscriptions = load_data(SUBSCRIPTIONS_FILE)
    for subscription in subscriptions:
        if subscription['customer_id'] == customer_id:
            return subscription
    return None
