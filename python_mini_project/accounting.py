import datetime
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from library import load_data, save_data

EXPENSES_FILE = 'expenses.json'


def add_expense(date, amount):
    expenses = load_data(EXPENSES_FILE)
    expense = {
        'date': date.isoformat(),
        'amount': amount
    }
    expenses.append(expense)
    save_data(expenses, EXPENSES_FILE)


def display_monthly_expenses_curve():
    expenses = load_data(EXPENSES_FILE)
    monthly_expenses = calculate_monthly_expenses(expenses)

    x = list(monthly_expenses.keys())
    y = list(monthly_expenses.values())

    plt.plot(x, y, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Expenses (TND)')
    plt.title('Monthly Expenses')
    plt.show()


def calculate_monthly_expenses(expenses):
    monthly_expenses = defaultdict(int)
    for expense in expenses:
        date = datetime.date.fromisoformat(expense['date'])
        year_month = (date.year, date.month)
        monthly_expenses[year_month] += expense['amount']
    return monthly_expenses


def load_subscriptions():
    with open('subscriptions.json', 'r') as file:
        return json.load(file)


def get_monthly_income():
    subscriptions = load_subscriptions()
    income_by_month = defaultdict(int)

    for subscription in subscriptions.values():
        start_date = datetime.strptime(subscription["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(subscription["end_date"], "%Y-%m-%d")
        months = (end_date.year - start_date.year) * \
            12 + end_date.month - start_date.month
        cost_per_month = 5  # Subscription cost per month (5 Tunisian Dinar)

        month_key = f"{start_date.year}-{str(start_date.month).zfill(2)}"
        income_by_month[month_key] += cost_per_month * months

    return dict(income_by_month)
