import json

with open("data/books.json") as book_data:
  books = json.load(book_data)