from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import payments as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_payment = model.Payment(
        order_id=request.order_id,
        card_number=request.card_number,
        card_holder=request.card_holder,
        expiration_date=request.expiration_date,
        payment_type=request.payment_type,
        amount=request.amount
    )
    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_payment

def read_all(db: Session):
    try:
        result = db.query(model.Payment).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, payment_id):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return payment

def update(db: Session, payment_id, request):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id)
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
        update_data = request.dict(exclude_unset=True)
        payment.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return payment.first()

def delete(db: Session, payment_id):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id)
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
        payment.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
