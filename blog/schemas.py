from pydantic import BaseModel  
from typing import List, Optional

class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True  # This allows Pydantic to read data as dictionaries from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # so that it can serialize it properly.

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True  # This allows Pydantic to read data as dictionaries from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # so that it can serialize it properly.

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []  # This will include the blogs created by the user
    class Config():
        orm_mode = True  # This allows Pydantic to read data as dictionaries from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # so that it can serialize it properly.

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser  # This will include the user who created the blog
    class Config():
        orm_mode = True  # This allows Pydantic to read data as dictionaries from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # so that it can serialize it properly.

class Login(BaseModel):
    email: str
    password: str

    class Config():
        orm_mode = True  # This allows Pydantic to read data as dictionaries from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # so that it can serialize it properly.

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config():
        orm_mode = True  # This allows Pydantic to read data as dictionaries from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # so that it can serialize it properly.

class TokenData(BaseModel):
    email: Optional[str] = None

    class Config():
        orm_mode = True  # This allows Pydantic to read data as dictionaries from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # so that it can serialize it properly.
        