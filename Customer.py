
class Customer:
    def __init__(self, name: str, surname: str, idno: int):
        self.__Name = name
        self.__Surname = surname
        self.__ID_NO = idno

    def get_name(self):
        return self.__Name

    def get_surname(self):
        return self.__Surname

    def get_ID(self):
        return self.__ID_NO

    def set_name(self, name: str):
        self.__Name = name

    def set_surname(self, surname: str):
        self.__Surname = surname

    def set_ID(self, idno: int):
        self.__ID_NO = idno



