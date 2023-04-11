from library import add_item, modify_item, delete_item, load_data
import json
BOOKS_FILE = 'books.json'


def add_book(book):
    add_item(book, BOOKS_FILE)


def modify_book(book_id, book):
    modify_item(book_id, book, BOOKS_FILE)


def delete_book(book_id):
    delete_item(book_id, BOOKS_FILE)


def search_books(criteria):
    books = load_data(BOOKS_FILE)
    results = []

    for book_id, book in books.items():
        matches = True
        for field, value in criteria.items():
            if field in book and value.lower() not in str(book[field]).lower():
                matches = False
                break

        if matches:
            results.append(book)

    return results
