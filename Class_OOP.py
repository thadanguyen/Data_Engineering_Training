from datetime import datetime
from datetime import date
from datetime import timedelta

class Person:
    def __init__(self, id, name, age, no_days_rent):
        self.name = name
        self.age = age
        self.id = id
        self.no_days_rent = no_days_rent
        self.vip = False
        self.start_date = date.today()
        self.end_date = self.start_date + timedelta(days = self.no_days_rent)
        self.room_type = None 

    def __str__(self):
        return f"ID: {self.id} Name: {self.name} VIP: {self.vip}"
    
    def calculate_rent(self):
        if self.room_type is None:
            return "No room assigned"
        rent_prc = self.no_days_rent * self.room_type.price
        return rent_prc
    
class VIP(Person): 
    def __init__(self, id, name, age, no_days_rent):
        super().__init__(id, name, age, no_days_rent)
        self.vip = True
        
    def calculate_rent(self):
        return super().calculate_rent() * 0.9
        
class Type():
    def __init__(self, type, price):
        self.type = type
        self.price = price
        
    def __str__(self):
        return f"Type: {self.type} Price: {self.price}"
        
class Room():
    def __init__(self, name, type_of_room):
        self.name = str(name)
        self.Type = type_of_room
        self.status = False
        self.tenant = None

    def take_tenants(self, person):
        self.tenant = person
        self.status = True
        person.room_type = self.Type
    
    def return_room(self):
        self.tenant = None
        self.status = False

    def __str__(self):
        return f"Room: {self.name} {self.Type} Occupied: {self.status}"

def show_room_types(type_lst):
    if len(type_lst) == 0:
        print("There are no room type!")
    else:
        for i, t in enumerate(type_lst, 1):
            print(f"{i}. {t}")

def find_room_type(type_lst, room_type):
    if len(type_lst) == 0:
        return None
    else:
        for t in type_lst:
            if t.type == room_type:
                return t

def find_room_based_on_type(room_lst, room_type):
    if len(room_lst) == 0:
        return None
    else:
        for r in room_lst:
            if (r.Type.type == room_type) and (~r.status):
                return r
    
def show_room_status(room_lst):
    if len(room_lst) == 0:
        return "There are no rooms!"
    else:
        result = ""
        for i, room in enumerate(room_lst, 1):
            result += f"{i}. {room}\n"
        return result
            
def show_guest_lst(guest_lst):
    if len(guest_lst) == 0:
        print("There are no guests!")
    else:
        for i, guest in enumerate(guest_lst, 1):
            print(f"{i}. {guest}")

def find_guest(guest_lst, id):
    if len(guest_lst) == 0:
        return None
    else:
        for guest in guest_lst:
            if guest.id == id:
                return guest
    return None 

def find_room_person(room_lst, person):
    for room in room_lst:
        if room.tenant.id == person.id:
            return room



def cal_revenue(guest_lst, start_date, end_date):
    total_revenue = 0
    start_date_trns = datetime.strptime(start_date, '%d/%m/%Y').date()
    end_date_trns = datetime.strptime(end_date, '%d/%m/%Y').date()
    for guest in guest_lst:
        if ((guest.end_date >= start_date_trns) and (guest.end_date <= end_date_trns)):
            total_revenue += guest.calculate_rent()
    return f"The total revenue from {start_date} to {end_date} is: {total_revenue}"

def add_room_type(type_lst, type_f, type_name, type_price):
    if type_f == 1:     
        type_lst.append(Type(type_name, type_price))
        return f"Successfully added {type_name} type!"
    elif type_f == 2:
        type_lst.remove(find_room_type(type_lst, type_name))
        return (f"Successfully removed {type_name} type!")
    
def add_guest(room_lst, guest_lst, guest_id, guest_name, guest_age, no_days_rent, vip_status, room_choice):
    if vip_status == 'y':
        new_guest = VIP(guest_id, guest_name, guest_age, no_days_rent)
    else: 
        new_guest = Person(guest_id, guest_name, guest_age, no_days_rent)
    find_room_based_on_type(room_lst, room_choice).take_tenants(new_guest)
    guest_lst.append(new_guest)
    return f"Successfully added new guest id {guest_id}!"

def rm_guest(room_lst, guest_lst, guest_id):
    if len(guest_lst) == 0:
        return "There are no guests!"
    else:
        rm_guest_id = find_guest(guest_lst, guest_id)
        if rm_guest_id is None:
            return "There is no guest with that id!"
        find_room_person(room_lst, rm_guest_id).return_room()
        guest_lst.remove(find_guest(guest_lst, guest_id))
        return f"Successfully removed guest id {guest_id}"

def cal_rent_id(guest_lst, guest_id): 
    guest = find_guest(guest_lst, guest_id)
    if guest == None:
        return "No guest with that id"
    rent = guest.calculate_rent()
    return f"The total rent price is: {rent}"

if __name__ == '__main__':
    type_lst = [Type("Normal", 1000)]
    room_lst = []
    guests_lst = []
    exit_to_menu = True
    while True:
        if exit_to_menu:
            f = int(input('''
                    0.Adding/Removing Type of room
                    1.Adding new room
                    2.Adding/Removing guest by ID numbers
                    3.Calculate room rental for guests
                    4.Show room status
                    5.Calculate revenue from specified start-end date
                    Choose function: '''))
            exit_to_menu = False
    
        if f == 0:
            print("Showing all room types")
            show_room_types(type_lst)
            type_f = int(input('''Do you want to add or remove room type?\n
                        1.Add new room type\n
                        2.Remove room type\n
                        3.Exit\n'''))
            type_price = None
            if type_f == 1 or type_f == 2:
                type_name = input("What is the type name? ")
                if type_f == 1:
                    type_price = int(input("What is its price? "))
                print(add_room_type(type_lst, type_f, type_name, type_price))
            exit_to_menu = True
                
        elif f == 1:
            print("Showing all rooms")
            show_room_status(room_lst)
            room_f = input('''Do you wanna add new room? [y/n] ''')
            if (room_f == 'y'):
                room_type = input("What is the type of room?") 
                room_name = input("What is its name?")
                room_lst.append(Room(room_name, find_room_type(type_lst, room_type)))
                print("Successfully added new room!")
            exit_to_menu = True
        
        elif f == 2:
            print("Showing all guests:")
            show_guest_lst(guests_lst)
            guest_f = int(input('''Do you want to add or remove guest?
                                1.Add guest
                                2.Remove guest
                                3.Exit'''))
            guest_id = input("What is the guest's id? ")
            if guest_f == 1:
                guest_name = input("What is their name? ")
                guest_age = input("How old are they? ")
                no_days_rent = int(input("How long will they stay? "))
                vip_status = input("Are they VIP? [y/n] ")
                room_choice = input("What room type will they have? ")
                print(add_guest(guests_lst, guest_id, guest_name, guest_age, no_days_rent, vip_status, room_choice))
            elif guest_f == 2:
                print(rm_guest(guests_lst, guest_id))
            exit_to_menu = True
        
        elif f == 3:
            print("Showing all guests: ")
            show_guest_lst(guests_lst)
            rent_f = input("What is the guest id? ")
            print(cal_rent_id(guests_lst, rent_f))
            exit_to_menu = True
            
        elif f == 4:
            print("Showing all rooms status")
            show_room_status(room_lst)
            exit_to_menu = True
        
        elif f == 5:
            inp_start = input("What is the start date (DD/MM/YYYY)? ")
            inp_end   = input("What is the end date (DD/MM/YYYY)? ")
            print(cal_revenue(guests_lst, inp_start, inp_end))
            exit_to_menu = True
            
        else:
            ttest = Type("Luxury", 10000)
            rtest = Room("202", ttest)
            gtest = VIP('1', 'dat', 20, 3)
            type_lst.append(ttest)
            room_lst.append(rtest)
            guests_lst.append(gtest)
            rtest.take_tenants(gtest)
            exit_to_menu = True
