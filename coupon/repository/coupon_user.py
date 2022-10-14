from sqlalchemy.orm import Session

from coupon.models.data.base_model import Coupon_User


class CouponUserRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_coupon_user(self, coupon_user: Coupon_User) -> bool:
        try:
            self.sess.add(coupon_user)
            self.sess.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def get_all_coupon_user(self):
        return self.sess.query(Coupon_User).all()

    def get_coupon_user(self, coupon_id: int, user_id: int):
        return self.sess.query(Coupon_User).filter(Coupon_User.user_id == user_id and
                                                   Coupon_User.coupon_id == coupon_id).one_or_none()
