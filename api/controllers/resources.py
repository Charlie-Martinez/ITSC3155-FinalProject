from sqlalchemy.orm import Session
from fastapi import HTTPException, Response
from ..models import resources as model

def create(db: Session, request):
    new_item = model.Resource(**request.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def read_all(db: Session):
    return db.query(model.Resource).all()

def read_one(db: Session, resource_id: int):
    item = db.query(model.Resource).filter(model.Resource.id == resource_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Resource not found")
    return item

def update(db: Session, resource_id: int, request):
    item = db.query(model.Resource).filter(model.Resource.id == resource_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Resource not found")
    item.update(request.dict(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, resource_id: int):
    item = db.query(model.Resource).filter(model.Resource.id == resource_id)
    if not item.first():
        raise HTTPException(status_code=404, detail="Resource not found")
    item.delete()
    db.commit()
    return Response(status_code=204)
