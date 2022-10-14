from fastapi import FastAPI

from coupon.api import login, signup, user, coupon_api

app = FastAPI()
app.include_router(login.router, prefix='/coupon')
app.include_router(signup.router, prefix='/coupon')
app.include_router(user.router, prefix='/coupon')
app.include_router(coupon_api.router, prefix='/coupon')
