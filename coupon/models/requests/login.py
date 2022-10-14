from pydantic import BaseModel


class LoginReq(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
