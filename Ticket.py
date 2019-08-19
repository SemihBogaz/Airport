from Airport.Customer import Customer
from Airport.Flight import Flight


class Ticket:
    def __init__(self, customer: Customer, flight: Flight, seat: str):
        self.__Customer = customer
        self.__Flight = flight
        self.__Seat = seat

    def __str__(self):
        ticket = """
        Name:\t{}
        Surname:\t{}
        ID:\t{}
        Flight Date:\t{}
        Flight Time:\t{}
        Seat:\t{}    
        """.format(self.__Customer.get_name(), self.__Customer.get_surname(), self.__Customer.get_ID(),
                   self.__Flight.get_date().date(), self.__Flight.get_date().time(), self.__Seat)
        return str(25*'=' + '\n' + ticket + '\n' + 25*'=')
