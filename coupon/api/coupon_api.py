from datetime import date

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from coupon.db_config.base_config import sess_db
from coupon.models.data.base_model import User, Coupon_User
from coupon.repository.coupon_repository import CouponRepository
from coupon.repository.coupon_user import CouponUserRepository
from coupon.repository.login import LoginRepository
from coupon.repository.user import UserRepository
from coupon.security.secure import http_basic

router = APIRouter()


@router.get("/coupons/")
async def get_coupons(credentials: HTTPBasicCredentials = Depends(http_basic),
                      sess: Session = Depends(sess_db)):
    repo: CouponRepository = CouponRepository(sess)
    result = repo.get_all_coupon()
    return result


@router.patch("/coupon/use/{coupon_id}")
async def use_coupon(coupon_id: int, credentials: HTTPBasicCredentials = Depends(http_basic),
                     sess: Session = Depends(sess_db)):
    coupon_repo: CouponRepository = CouponRepository(sess)
    user_repo: UserRepository = UserRepository(sess)
    login_repo: LoginRepository = LoginRepository(sess)
    coupon_user_repo: CouponUserRepository = CouponUserRepository(sess)
    login = login_repo.get_all_login_username(credentials.username)
    coupon = coupon_repo.get_coupon(coupon_id)

    if coupon.expire_time < date.today():
        return JSONResponse(content={'message': 'The coupon is expired'}, status_code=406)
    if coupon.capacity_of_use == 0:
        return JSONResponse(content={'message': 'The coupon is not valid'}, status_code=406)

    user = user_repo.get_user(login.id)

    if coupon_user_repo.get_coupon_user(coupon_id=coupon.id, user_id=user.id):
        return JSONResponse(content={'message': 'You have used this coupon before'}, status_code=406)

    user_repo.update_user(user.id, {User.balance: User.balance + coupon.value})
    coupon_user_repo.insert_coupon_user(Coupon_User(coupon_id=coupon.id, user_id=user.id))
