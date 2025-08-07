""" Test main.py """
from starlette.testclient import TestClient
from app.books import app, BOOKS

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_read_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "title": "Computer Science Pro",
            "author": "codingwithroby",
            "description": "A very nice book!",
            "rating": 5,
        },
        {
            "id": 2,
            "title": "Be Fast with FastAPI",
            "author": "codingwithroby",
            "description": "A great book!",
            "rating": 5,
        },
        {
            "id": 3,
            "title": "Master Endpoints",
            "author": "codingwithroby",
            "description": "A awesome book!",
            "rating": 5,
        },
        {
            "id": 4,
            "title": "HP1",
            "author": "Author 1",
            "description": "Book Description",
            "rating": 2,
        },
        {
            "id": 5,
            "title": "HP2",
            "author": "Author 2",
            "description": "Book Description",
            "rating": 3,
        },
        {
            "id": 6,
            "title": "HP3",
            "author": "Author 3",
            "description": "Book Description",
            "rating": 1,
        },
    ]
