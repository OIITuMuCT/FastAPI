from books import BOOKS

def update_book(book_id):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id+1:
            print(BOOKS[book_id])
        
# update_book(3)


def book_list(book_id):
    for i, book in enumerate(BOOKS, 1):
        if book_id == i:
            print(f'Book: {i} - title: {book}')
    

book_list(2)