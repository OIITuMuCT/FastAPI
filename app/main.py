from fastapi import FastAPI
from data_books import BOOKS

app = FastAPI()

@app.get('/api-endpoint')
async def first_api():
    return {'message': 'Hello Sergio!'}


@app.get("/books")
async def read_all_books():
    return BOOKS



@app.get("/books/{book_title}/")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
