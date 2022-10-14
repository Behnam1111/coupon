from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session

from coupon.db_config.base_config import sess_db
from coupon.repository.user import UserRepository
from coupon.security.secure import http_basic

router = APIRouter()


@router.get("/user/{id}")
async def get_user(id: int, credentials: HTTPBasicCredentials = Depends(http_basic),
                   sess: Session = Depends(sess_db)):
    repo: UserRepository = UserRepository(sess)
    result = repo.get_user(id)
    return result
