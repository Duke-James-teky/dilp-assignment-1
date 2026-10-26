from fastapi import FastAPI #import FastAPI from fastapi module

# Create an instance of the FastAPI class
#  and assign it to the Variable app

app = FastAPI()

# use the app instance to define a route for the home page
@app.get("/")
def home():
    return {"message": "hello duke, so how are you doing"}