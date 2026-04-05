from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import ratings as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_rating = model.Rating(
        customer_id=request.customer_id,
        order_id=request.order_id,
        rating=request.rating,
        review_text=request.review_text
    )
    try:
        db.add(new_rating)
        db.commit()
        db.refresh(new_rating)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_rating

def read_all(db: Session):
    try:
        result = db.query(model.Rating).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, rating_id):
    try:
        rating = db.query(model.Rating).filter(model.Rating.id == rating_id).first()
        if not rating:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return rating

def update(db: Session, rating_id, request):
    try:
        rating = db.query(model.Rating).filter(model.Rating.id == rating_id)
        if not rating.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
        update_data = request.dict(exclude_unset=True)
        rating.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return rating.first()

def delete(db: Session, rating_id):
    try:
        rating = db.query(model.Rating).filter(model.Rating.id == rating_id)
        if not rating.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
        rating.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
