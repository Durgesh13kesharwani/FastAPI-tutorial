from fastapi import FastAPI
from . import models
from .database import engine
# from .hashing import Hash
from .routers import blog, user, authentication

app= FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
# def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     blog.update(request.dict())
#     db.commit()
#     return 'updated successfully'

# @app.get("/blog", response_model= List[schemas.ShowBlog], tags=["Blogs"])
# def all(db: Session = Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# @app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=["Blogs"]) 
# def show(id: int, response=Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")   
#     return blog



# @app.post("/user", response_model= schemas.ShowUser, tags=["Users"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password= Hash.bcrypt(request.password))
#     # Ensure that the password is hashed before storing it
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=["Users"])
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
#     return user