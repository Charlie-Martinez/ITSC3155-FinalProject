from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)

@router.post("/", response_model=schema.Recipe)
def create(request: schema.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.Recipe])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{recipe_id}", response_model=schema.Recipe)
def read_one(recipe_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, recipe_id)

@router.put("/{recipe_id}", response_model=schema.Recipe)
def update(recipe_id: int, request: schema.RecipeUpdate, db: Session = Depends(get_db)):
    return controller.update(db, recipe_id, request)

@router.delete("/{recipe_id}")
def delete(recipe_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, recipe_id)
