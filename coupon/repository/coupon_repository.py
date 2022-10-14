from typing import Dict, Any

from sqlalchemy.orm import Session

from coupon.models.data.base_model import Coupon


class CouponRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_coupon(self, coupon: Coupon) -> bool:
        try:
            self.sess.add(coupon)
            self.sess.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def update_coupon(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Coupon).filter(Coupon.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_coupon(self, id: int) -> bool:
        try:
            self.sess.query(Coupon).filter(Coupon.id == id).delete()
            self.sess.commit()
        except:
            return False
        return True

    def get_all_coupon(self):
        return self.sess.query(Coupon).all()

    def get_coupon(self, id: int):
        return self.sess.query(Coupon).filter(Coupon.id == id).one_or_none()

    def get_coupon_by_code(self, code):
        return self.sess.query(Coupon).filter(Coupon.code == code).one_or_none()
