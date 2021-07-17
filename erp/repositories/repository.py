import string

import dataset


class Repository:

    __db_name__ = 'data/mini_erp.db'

    def __init__(self, table: string):
        self.__table_name__ = table

    def get_one(self, oid: int):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            record = db[self.__table_name__].find_one(id=oid)

            if record:
                return record
            else:
                return False

    def get_all(self):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            records = db[self.__table_name__].all()

            if records:
                return records
            else:
                return False

    def add(self, model: dict):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            record = db[self.__table_name__].insert(model)

            if record:
                return record
            else:
                return False

    def update(self, model: dict):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            record = db[self.__table_name__].update(model, ['id'])

            if record:
                return record
            else:
                return False

    def remove(self, oid: int):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            record = db[self.__table_name__].delete(id=oid)

            if record:
                return record
            else:
                return False

    def find(self, **params):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            record = db[self.__table_name__].find_one(params)

            if record:
                return record
            else:
                return False

    def find_all(self, **params):
        with dataset.connect('sqlite:///{}'.format(self.__db_name__)) as db:
            record = db[self.__table_name__].all(params)

            if record:
                return record
            else:
                return False
