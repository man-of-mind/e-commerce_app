from fastapi import FastAPI, status, HTTPException, Depends
from . import database, models, schemas
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.get('/all-categories', status_code=status.HTTP_200_OK, response_model=List[schemas.AllCategories])
def allCategories(db: Session = Depends(database.get_db)):
    all_categories = db.query(models.All_categories).order_by(models.All_categories.id).all()
    if all_categories:
        return all_categories
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No categories found")

@app.post('/category/add', response_model= schemas.AllCategories)
def addCategory(request: schemas.Categories, db: Session = Depends(database.get_db)):
    try:
        new_category = models.All_categories(name=request.name)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Category already exist")
    