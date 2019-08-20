from random import randint


class Cities:
    def __init__(self, name: str):
        self.__Name = name
        self.__Temperature = randint(18, 25)
        self.__Weather = ["Sunny", "Rainy", "Foggy", "Windy"][randint(0, 3)]

    def get_name(self):
        return self.__Name

    def set_name(self, name):
        self.__Name = name

    def get_temp(self):
        return self.__Temperature

    def get_weather(self):
        return self.__Weather

    def __str__(self):
        return self.__Name

    # did not create setter methods for temp & weather
