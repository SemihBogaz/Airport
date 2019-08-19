from datetime import datetime
from Airport.Cities import Cities


class Flight:
    def __init__(self, departure: Cities, destination: Cities, dates: datetime):
        self.__Destination = destination
        self.__Departure = departure
        self.__Dates = dates

    def tardiness(self, minutes: int):
        Day = self.__Dates.day
        Hour = self.__Dates.hour
        Minute = self.__Dates.minute

        if (Minute + minutes) >= 60:
            Hour += int((Minute + minutes) / 60)
            Minute = (Minute + minutes) % 60

            if Hour >= 24:
                Day += int(Hour / 24)
                Hour = Hour % 24

        newDate = datetime(self.__Dates.year, self.__Dates.month, Day, Hour, Minute)
        self.__Dates = newDate

    def get_date(self):
        return self.__Dates


# x = Flight(Cities("İstanbul"), Cities("İzmir"), datetime(2019, 8, 2, 7, 40))
# print(str(x.get_date().hour) + "." + str(x.get_date().minute))
# x.tardiness(int(30))
# print(str(x.get_date().hour) + "." + str(x.get_date().minute))
#



