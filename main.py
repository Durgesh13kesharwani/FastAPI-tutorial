from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 
import uvicorn

app= FastAPI() # Create an instance of FastAPI

@app.get("/blog") # Define a route for the root path #("/") this is path # get("/") this is called operation on the path # get, post, delete, put are the HTTP methods # @app.get("/") this is called path operation decorator
def read_root(limit=10, published:bool = True, sort: Optional[str]=None): # Function to handle GET requests to the root path # this is called as path operation function
    #only get 10 published blogs
    if published:
        return {"data": f'{limit} published blogs from the db'}
    else:
        return {"data": f'{limit} blogs from the db'} # This function returns a JSON response with a greeting message

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}

@app.get("/blog/{id}")
def show(id: int):
    #fetch blog by id=id
    return {"data": id} 

@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    #fetch comments for blog by id=id
    return limit
    return {"data":{'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published:  Optional[bool] = True  # Default value for published is True

@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f'Blog is created with title {blog.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1",port=9000)