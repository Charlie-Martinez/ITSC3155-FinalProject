from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.util import ordered_column_set

from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError
from ..models import promotions as promotion_model
from datetime import datetime

def create(db: Session, request):
    new_order = model.Order(
        customer_name=request.customer_name,
        description=request.description,
        tracking_number=request.tracking_number,
        delivery_type=request.delivery_type,
        total_price=request.total_price,
        customer_id=request.customer_id,
        promotion_id=request.promotion_id,
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_order


def read_all(db: Session, start_date=None, end_date=None):
    try:
        query = db.query(model.Order)

        if start_date:
            start_date = datetime.fromisoformat(start_date)
            query = query.filter(model.Order.order_date >= start_date)

        if end_date:
            end_date = datetime.fromisoformat(end_date)
            query = query.filter(model.Order.order_date <= end_date)

        result = query.all()

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return result

def read_one(db: Session, order_id):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order

def read_by_tracking(db: Session, tracking_number: str):
    try:
        order = db.query(model.Order).filter(model.Order.tracking_number == tracking_number).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order

def apply_promo(db: Session, order_id: int, promo_code: str):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id).first()

        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")

        promo = db.query(promotion_model.Promotion).filter(
            promotion_model.Promotion.promo_code == promo_code
        ).first()

        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promo not found!")

        if not promo.is_active:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Promo is not active!")

        discount = float(promo.discount_value) / 100
        order.total_price = float(order.total_price) - (float(order.total_price) * discount)
        order.promotion_id = promo.id

        db.commit()
        db.refresh(order)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return order

def update(db: Session, order_id, request):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        update_data = request.dict(exclude_unset=True)
        order.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order.first()


def delete(db: Session, order_id):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        order.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
