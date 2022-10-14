from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from coupon.db_config.base_config import sess_db
from coupon.models.data.base_model import Signup
from coupon.models.requests.signup import SignupReq
from coupon.repository.signup import SignupRepository

router = APIRouter()


@router.post("/signup/add")
def add_signup(req: SignupReq,
               sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    signup = Signup(password=req.password, username=req.username)
    result = repo.insert_signup(signup)
    if result == True:
        return signup
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)
