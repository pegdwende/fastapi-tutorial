

from fastapi import Depends, status, HTTPException, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schema, helper
from ..config import settings
from fastapi.logger import logger
import logging
router = APIRouter(prefix="/users", tags=['Users'])


@router.post("/", status_code=status.HTTP_201_CREATED,  response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    # logger.setLevel(logging.DEBUG)
    # logger.error(settings.database_hostname)
    # logger.error(settings.database_username)

    hashed_password = helper.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schema.CreatedUser)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        #     response.status_code = status.HTTP_404_NOT_FOUND
        #     return {'message': f"post with id :{id} was not found"}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"User with id :{id} does not exist")

    return user
