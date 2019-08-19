from datetime import datetime

from Airport.Cities import Cities
from Airport.Flight import Flight
from Airport.Customer import Customer
from Airport.Ticket import Ticket

ticket1 = Ticket(Customer("John", "Doe", 1234), Flight(Cities("NewYork"), Cities("London"), datetime(2019,7,7,12,6)), "43B")
print(ticket1)
