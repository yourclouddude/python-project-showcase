"""Persistent local API. Run: uvicorn main:app --host 127.0.0.1"""
import os
import sqlite3
from decimal import Decimal
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

class BookInput(BaseModel):
    title: str = Field(min_length=1, max_length=120, pattern=r"\S")
    author: str = Field(min_length=1, max_length=120, pattern=r"\S")
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    available: bool = True
    model_config = {"extra": "forbid"}

def create_app(database="books.db"):
    app = FastAPI(title="Bookstore learning API")
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, price TEXT, available INTEGER)")

    def rows(query, parameters=()):
        with sqlite3.connect(database) as connection:
            connection.row_factory = sqlite3.Row
            return [dict(row) | {"available": bool(row["available"])} for row in connection.execute(query, parameters)]

    @app.get("/books")
    def get_books():
        return rows("SELECT * FROM books ORDER BY id")

    @app.get("/books/{book_id}")
    def get_book(book_id: int):
        found = rows("SELECT * FROM books WHERE id=?", (book_id,))
        if not found:
            raise HTTPException(404, "Book not found")
        return found[0]

    @app.post("/books", status_code=201)
    def add_book(book: BookInput):
        with sqlite3.connect(database) as connection:
            cursor = connection.execute("INSERT INTO books(title,author,price,available) VALUES (?,?,?,?)", (book.title.strip(), book.author.strip(), str(book.price), int(book.available)))
            book_id = cursor.lastrowid
        return get_book(book_id)

    @app.put("/books/{book_id}")
    def update_book(book_id: int, book: BookInput):
        get_book(book_id)
        with sqlite3.connect(database) as connection:
            connection.execute("UPDATE books SET title=?,author=?,price=?,available=? WHERE id=?", (book.title.strip(), book.author.strip(), str(book.price), int(book.available), book_id))
        return get_book(book_id)

    @app.delete("/books/{book_id}", status_code=204)
    def delete_book(book_id: int):
        with sqlite3.connect(database) as connection:
            if connection.execute("DELETE FROM books WHERE id=?", (book_id,)).rowcount == 0:
                raise HTTPException(404, "Book not found")
        return Response(status_code=204)
    return app

app = create_app(os.environ.get("BOOKS_DB", "books.db"))
