from typing import Dict, Any

from sqlalchemy.orm import Session

from coupon.models.data.base_model import Login, User


class UserRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_user(self, user: User) -> bool:
        try:
            self.sess.add(user)
            self.sess.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def update_user(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Login).filter(User.id == id).update(details, synchronize_session='fetch')
            self.sess.commit()
        except:
            return False
        return True

    def delete_user(self, id: int) -> bool:
        try:
            self.sess.query(User).filter(User.id == id).delete()
            self.sess.commit()
        except:
            return False
        return True

    def get_all_user(self):
        return self.sess.query(Login).all()

    def get_user(self, id: int):
        return self.sess.query(User).filter(User.id == id).one_or_none()
