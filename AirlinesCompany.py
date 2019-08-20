import datetime
from Airport.Customer import Customer
from Airport.Cities import Cities
from Airport.Ticket import Ticket
from Airport.Flight import Flight


class Company:
    def __init__(self):
        self.__activeFlights = list()
        self.__passiveFlights = list()
        self.__activeTickets = list()
        self.__passiveTickets = list()

    def add_ticket(self, customer: Customer, flight: Flight, seat: str):
        if flight in self.__activeFlights:
            ticket = Ticket(customer, flight, seat)
            self.__activeTickets.append(ticket)
            return ticket

    def cancel_ticket(self, ticket: Ticket):
        if ticket in self.__activeTickets:
            self.__activeTickets.remove(ticket)

    def add_flight(self, departure: Cities, destination: Cities, dates: datetime):
        flight = Flight(departure, destination, dates)
        self.__activeFlights.append(flight)
        return flight

    def flight_occur(self, flight: Flight):
        for ticket in self.__activeTickets:
            if ticket.get_flight() == flight:
                self.__activeTickets.remove(ticket)
                self.__passiveTickets.append(ticket)

        self.__activeFlights.remove(flight)
        self.__passiveFlights.append(flight)

    def tardiness(self, flight: Flight, minute: int):
        flight.tardiness(minute)
