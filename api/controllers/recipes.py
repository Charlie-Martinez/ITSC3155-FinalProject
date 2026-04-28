from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import recipes as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.Recipe(**request.dict())
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__['orig']))
    return new_item

def read_all(db: Session):
    return db.query(model.Recipe).all()

def read_one(db: Session, recipe_id: int):
    item = db.query(model.Recipe).filter(model.Recipe.id == recipe_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return item

def update(db: Session, recipe_id: int, request):
    item = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Recipe not found")
    item.update(request.dict(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, recipe_id: int):
    item = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Recipe not found")
    item.delete()
    db.commit()
    return Response(status_code=204)
