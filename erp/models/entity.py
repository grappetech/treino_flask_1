class Entity:
    def __init__(self):
        return

    __id__: int

    def get_id(self):
        return self.__id__

    def set_id(self, id: int):
        self.__id__ = id
