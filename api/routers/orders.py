from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Order])
def read_all(start_date: str = None, end_date: str = None, db: Session = Depends(get_db)):
    return controller.read_all(db=db, start_date=start_date, end_date=end_date)


@router.post("/{order_id}/apply-promo", response_model=schema.Order)
def apply_promo(order_id: int, promo_code: str, db: Session = Depends(get_db)):
    return controller.apply_promo(db=db, order_id=order_id, promo_code=promo_code)


@router.get("/track/{tracking_number}", response_model=schema.Order)
def read_by_tracking(tracking_number: str, db: Session = Depends(get_db)):
    return controller.read_by_tracking(db=db, tracking_number=tracking_number)


@router.get("/revenue")
def daily_revenue(date: str, db: Session = Depends(get_db)):
    return controller.daily_revenue(db=db, date=date)


@router.get("/{order_id}", response_model=schema.Order)
def read_one(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=order_id)


@router.put("/{order_id}", response_model=schema.Order)
def update(order_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_id=order_id)


@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=order_id)
