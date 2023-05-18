from Class_OOP import *
import unittest
from datetime import date
from datetime import timedelta

class TestHotelManagement(unittest.TestCase):
    
    def setUp(self):
        #Initialize all objects for different test case
        self.type_lst = []
        self.room_lst = []
        self.guests_lst = []
        self.ttest = Type("Luxury", 10000)
        self.rtest = Room("202", self.ttest)
        self.rtest2 = Room("203", self.ttest)
        self.gtest = VIP('3', 'dat', 20, 3)
        self.type_lst.append(self.ttest)
        self.room_lst.append(self.rtest)
        self.room_lst.append(self.rtest2)
        self.guests_lst.append(self.gtest)
        self.rtest.take_tenants(self.gtest)
        
    def test_add_room_type(self):
        args = (self.type_lst, 1, "Normal", 1000)
        self.assertEqual(add_room_type(*args), "Successfully added Normal type!")
        args = (self.type_lst, 2, "Normal", None)
        self.assertEqual(add_room_type(*args), "Successfully removed Normal type!")
    
    def test_add_guest(self):
        args = (self.room_lst, self.guests_lst, '1', 'Thanh Dat', '20' , 3, "y", "Luxury")
        self.assertEqual(add_guest(*args), "Successfully added new guest id 1!")

    def test_remove_guest(self):
        args = (self.room_lst, self.guests_lst, '5')
        self.assertEqual(rm_guest(*args), "There is no guest with that id!")
        args = (self.room_lst, self.guests_lst, '3')
        self.assertEqual(rm_guest(*args), "Successfully removed guest id 3")
        args = (self.room_lst, [], '3')
        self.assertEqual(rm_guest(*args), "There are no guests!")
        
    
    def test_cal_rent_id(self):
        args = (self.guests_lst, '3')
        self.assertEqual(cal_rent_id(*args), "The total rent price is: 27000.0")
        args = (self.guests_lst, '5')
        self.assertEqual(cal_rent_id(*args), "No guest with that id")
    
    def test_show_room_status(self):
        self.assertEqual(show_room_status(self.room_lst), "1. Room: 202 Type: Luxury Price: 10000 Occupied: True\n2. Room: 203 Type: Luxury Price: 10000 Occupied: False\n")
        self.assertEqual(show_room_status([]), "There are no rooms!")
    
    def test_cal_revenue(self):
        start_date = date.today().strftime("%d/%m/%Y")
        end_date = (date.today() + timedelta(days = 5)).strftime("%d/%m/%Y")
        args = (self.guests_lst, start_date, end_date)
        self.assertEqual(cal_revenue(*args), f"The total revenue from {start_date} to {end_date} is: 27000.0")
        args = (self.guests_lst, "18/05/2022", "20/05/2022")
        self.assertEqual(cal_revenue(*args), f"The total revenue from 18/05/2022 to 20/05/2022 is: 0")

if __name__ == '__main__':
    unittest.main(verbosity=2)