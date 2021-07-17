import string
import dataset

from flask_bcrypt import Bcrypt
from erp.models.user import User
from erp.repositories.repository import Repository
from utils import util


class UserRepository(Repository):
    def __init__(self):
        super().__init__('users')

    def add(self, model: User):
        model.set_password(util.as_password(model.get_password()))
        return super(UserRepository, self).add(model)

    def validate(self, username: string, password: string):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            record = db[self.__table_name__].find_one(username=username)

            if record:
                return Bcrypt().check_password_hash(record['password'], password)
            else:
                return False



