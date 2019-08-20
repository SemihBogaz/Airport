from Airport import Customer, Flight


class Ticket:
    def __init__(self, customer: Customer, flight: Flight, seat: str):
        self.__Customer = customer
        self.__Flight = flight
        self.__Seat = seat

    def __str__(self):
        ticket = """
        Name:         {}
        Surname:      {}
        ID:           {}
        Flight Date:  {}
        Flight Time:  {}
        Seat:         {}
        Departure:    {}
        Destination:  {}  
        """.format(self.__Customer.get_name(), self.__Customer.get_surname(), self.__Customer.get_ID(),
                   self.__Flight.get_date().date(), self.__Flight.get_date().time(), self.__Seat,
                   self.__Flight.get_depar(), self.__Flight.get_dest())
        return str(100*'=' + '\n' + ticket + '\n' + 100*'=')

    def get_flight(self):
        return self.__Flight
