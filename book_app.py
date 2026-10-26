from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

# create a dict to store the books in memory
books = {}

#Create a dict to store book data
book_data = {"id": 0, "title": "", "author": "", "year": 0, "pages": 0, "languae": ""}

@app.get("/")
def home():
    return {"message": "Hello From the book api"}

#Get all the books
@app.get("/books")
def get_books():
    return books

@app.get("/books/{id}")
def get_book_by_id(id: str):
    book = books.get(id)
    if not book:
        return {"message": "book not found"}
    return book

@app.post("/books") #POST method to create a new resource
def add_book(
 title: str, author: str, year: int, pages: int, language: str
):
    new_book = book_data.copy()
    new_book["id"] = str(UUID(int=len(books)+1))
    new_book["title"] = title
    new_book["author"] = author
    new_book["year"] = year
    new_book["pages"] = pages
    new_book["language"] = language

    books[new_book["id"]] = new_book
    return {"message": "Book added successfully", "data": new_book}

# update book
@app.put("/books/{id}")
def update_book(
    id:str, title: str, author: str, year: int, page: int, language: str
):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}

    book["title"] = title
    book["author"] = author
    book["year"] = year
    book["pages"] = page
    book["language"] = language

    return {"message": "Book updatd successfully", "data": book}

# delete
@app.delete("/books/{id}")
def delete_book(id:str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}

    del book[id]

    return {"message": "Book deleted successfully"}
    
