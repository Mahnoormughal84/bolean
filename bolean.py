def can_enter_library(is_member: bool, has_overdue_books: bool) -> bool:
    """
    Determines if a user can enter the library.
    
    Parameters:
    is_member (bool): Whether the user is a registered library member.
    has_overdue_books (bool): Whether the user has overdue books.
    
    Returns:
    bool: True if the user can enter, False otherwise.
    """
    return is_member and not has_overdue_books


print(can_enter_library(True, False)) 
print(can_enter_library(True, True))  
print(can_enter_library(False, False)) 
print(can_enter_library(False, True))  

# 2. **Smart Home Lights:**
# A smart light turns on if it is dark OR someone is in the room. Write a function
# `should_light_turn_on(is_dark, person_present)` that returns True or False.

def should_light_turn_on(is_dark, person_present):
    return is_dark or person_present


print(should_light_turn_on(True, False)) 
print(should_light_turn_on(False, True))  
print(should_light_turn_on(False, False)) 
print(should_light_turn_on(True, True))   

#3. **Email Notification Settings:**
 #A user receives notifications if they have enabled email alerts AND their inbox is not full.
#Implement `should_notify(email_alerts_on, inbox_full)`.

def should_notify(email_alerts_on: bool, inbox_full: bool) -> bool:
    """
    Determines whether a user should receive an email notification.
    
    Parameters:
    email_alerts_on (bool): Whether the user has enabled email alerts.
    inbox_full (bool): Whether the user's inbox is full.
    
    Returns:
    bool: True if the user should receive a notification, False otherwise.
    """
    return email_alerts_on and not inbox_full

print(should_notify(True, False)) 
print(should_notify(True, True))   
print(should_notify(False, False)) 
print(should_notify(False, True))  


#4. **Weekend Discount Eligibility:**
# A shop gives discounts on weekends OR if a customer is a VIP member. Write a function
#`get_discount(is_weekend, is_vip)`.

def get_discount(is_weekend: bool, is_vip: bool) -> bool:
    """
    Determines if a customer is eligible for a discount.
    A discount is given if it is the weekend OR the customer is a VIP.

    :param is_weekend: Boolean indicating if it is the weekend.
    :param is_vip: Boolean indicating if the customer is a VIP member.
    :return: True if the customer gets a discount, False otherwise.
    """
    return is_weekend or is_vip
print(get_discount(True, False)) 
print(get_discount(False, True)) 
print(get_discount(False, False)) 


#5. **Door Lock System:**
 #A door unlocks if the correct pin is entered AND the user is authorized. Write a function
#`can_unlock(entered_pin, correct_pin, is_authorized)`. 

def can_unlock(entered_pin: str, correct_pin: str, is_authorized: bool) -> bool:
    """
    Determines if the door should unlock based on the entered PIN and authorization status.
    
    :param entered_pin: The PIN entered by the user.
    :param correct_pin: The correct PIN for the door lock.
    :param is_authorized: Boolean indicating whether the user is authorized.
    :return: True if the door should unlock, False otherwise.
    """
    return entered_pin == correct_pin and is_authorized
print(can_unlock("1234", "1234", True))  
print(can_unlock("1234", "5678", True)) 
print(can_unlock("1234", "1234", False)) 


#Boolean Logic - AND, OR, NOT (Medium)
#1. **Online Exam Eligibility:**
 #A student can take an online exam if they have registered AND have not been disqualified. Write a
#function `can_take_exam(registered, disqualified)`.

def can_take_exam(registered: bool, disqualified: bool) -> bool:
    """
    Determines if a student can take an online exam.
    
    A student can take the exam if they are registered AND have not been disqualified.
    
    :param registered: Boolean indicating if the student is registered.
    :param disqualified: Boolean indicating if the student is disqualified.
    :return: True if the student can take the exam, False otherwise.
    """
    return registered and not disqualified
print(can_take_exam(True, False))  
print(can_take_exam(True, True))   
print(can_take_exam(False, False)) 
print(can_take_exam(False, True))  


#2. **Smart Sprinkler System:**
# The sprinkler turns on if it's hot AND dry, OR if the moisture level is below 30%. Write
#`should_sprinkle(is_hot, is_dry, moisture_level)`.

def should_sprinkle(is_hot: bool, is_dry: bool, moisture_level: int) -> bool:
    """
    Determines if the sprinkler should turn on.
    
    The sprinkler turns on if:
    - It's both hot AND dry
    - OR if the moisture level is below 30%
    
    :param is_hot: Boolean indicating if it's hot
    :param is_dry: Boolean indicating if it's dry
    :param moisture_level: Integer representing the moisture level percentage
    :return: Boolean indicating if the sprinkler should turn on
    """
    return (is_hot and is_dry) or (moisture_level < 30)
print(should_sprinkle(True, True, 40))  
print(should_sprinkle(False, True, 25)) 
print(should_sprinkle(True, False, 35)) 
print(should_sprinkle(False, False, 20)) 



#3. **Theater Booking System:**
 #A customer can book a VIP seat if they have a VIP membership OR if they purchase a premium
#ticket. Write `can_book_vip(vip_member, premium_ticket)`.

def can_book_vip(vip_member: bool, premium_ticket: bool) -> bool:
    """
    Determines if a customer can book a VIP seat.
    
    Parameters:
    vip_member (bool): Whether the customer has a VIP membership.
    premium_ticket (bool): Whether the customer has purchased a premium ticket.
    
    Returns:
    bool: True if the customer can book a VIP seat, False otherwise.
    """
    return vip_member or premium_ticket
print(can_book_vip(True, False))  
print(can_book_vip(False, True))  
print(can_book_vip(False, False)) 

#4. **Security Camera Activation:**
 #A camera records if motion is detected AND it is nighttime OR if security mode is on. Implement
#`should_record(motion_detected, is_night, security_mode)`.

def should_record(motion_detected: bool, is_night: bool, security_mode: bool) -> bool:
    """
    Determines whether the security camera should record.
    
    Parameters:
    - motion_detected (bool): True if motion is detected.
    - is_night (bool): True if it is nighttime.
    - security_mode (bool): True if security mode is on.
    
    Returns:
    - bool: True if the camera should record, False otherwise.
    """
    return (motion_detected and is_night) or security_mode
print(should_record(True, False, True))  
print(should_record(False, True, False)) 
print(should_record(True, True, False))  
print(should_record(False, False, True)) 


#5. **Discount Eligibility Check:**
 #A store offers a 20% discount if a customer is a loyalty member AND has spent more than $100
#OR if they have a special coupon. Write `get_discount(loyalty_member, amount_spent,
#has_coupon)`.

def get_discount(loyalty_member, amount_spent, has_coupon):
    """
    Determines if a customer is eligible for a discount.

    Parameters:
    loyalty_member (bool): Whether the customer is a loyalty member.
    amount_spent (float): The total amount spent by the customer.
    has_coupon (bool): Whether the customer has a special coupon.

    Returns:
    bool: True if eligible for a discount, False otherwise.
    """
    return (loyalty_member and amount_spent > 100) or has_coupon
print(get_discount(True, 120, False))  
print(get_discount(False, 50, True))   
print(get_discount(True, 80, False))   
print(get_discount(False, 150, False)) 


#Boolean Logic - AND, OR, NOT (Hard)
#1. **Online Multiplayer Game Access:**
 #A player can join a match if they have an active subscription AND are not banned OR if they have
#a guest pass. Write `can_play_game(subscription_active, banned, guest_pass)`.

def can_play_game(subscription_active: bool, banned: bool, guest_pass: bool) -> bool:
    """
    Determines if a player can join a match based on their subscription status,
    ban status, and guest pass availability.
    
    A player can join if:
    - They have an active subscription AND are NOT banned OR
    - They have a guest pass
    
    :param subscription_active: Boolean indicating if the player has an active subscription
    :param banned: Boolean indicating if the player is banned
    :param guest_pass: Boolean indicating if the player has a guest pass
    :return: True if the player can join the match, False otherwise
    """
    return (subscription_active and not banned) or guest_pass
print(can_play_game(True, False, False))  
print(can_play_game(True, True, False))  
print(can_play_game(False, False, True))  
print(can_play_game(False, True, False))  
print(can_play_game(True, False, True))   


#2. **AI Chatbot Response:**
 #A chatbot responds to a user only if the user is not blocked AND the AI confidence score is above
#70%. Write `should_respond(is_blocked, confidence_score)`.
def should_respond(is_blocked: bool, confidence_score: float) -> bool:
    return not is_blocked and confidence_score > 70.0
print(should_respond(False, 85))  
print(should_respond(True, 80))   
print(should_respond(False, 60))  

#3. **Traffic Light System:**
 #A traffic light turns green if the road is clear AND the emergency vehicle is not nearby, OR if the
#manual override is activated. Implement `should_turn_green(road_clear, emergency_near,
#manual_override)`.

def should_turn_green(road_clear: bool, emergency_near: bool, manual_override: bool) -> bool:
    """
    Determines whether the traffic light should turn green based on given conditions.
    
    :param road_clear: True if the road is clear, otherwise False.
    :param emergency_near: True if an emergency vehicle is nearby, otherwise False.
    :param manual_override: True if the manual override is activated, otherwise False.
    :return: True if the traffic light should turn green, otherwise False.
    """
    return (road_clear and not emergency_near) or manual_override
print(should_turn_green(True, False, False))  
print(should_turn_green(True, True, False))   
print(should_turn_green(False, False, True))  


#4. **Hotel Room Booking:**
# A hotel allows room booking if the guest has valid ID AND a credit card OR a prior reservation.
#Write `can_book_room(valid_id, has_credit_card, prior_reservation)`.

def can_book_room(valid_id: bool, has_credit_card: bool, prior_reservation: bool) -> bool:
    """
    Determines if a hotel room can be booked based on the provided conditions.
    
    :param valid_id: Boolean indicating if the guest has a valid ID.
    :param has_credit_card: Boolean indicating if the guest has a credit card.
    :param prior_reservation: Boolean indicating if the guest has a prior reservation.
    :return: True if the guest can book a room, otherwise False.
    """
    return valid_id and (has_credit_card or prior_reservation)
print(can_book_room(True, True, False))  
print(can_book_room(True, False, True)) 
print(can_book_room(True, False, False)) 
print(can_book_room(False, True, True))  


#5. **Cybersecurity System:**
 #A login attempt is blocked if the IP is blacklisted OR the password is incorrect AND 3 failed
#attempts have been made. Implement `is_login_blocked(ip_blacklisted, correct_password,
#failed_attempts)`.

def is_login_blocked(ip_blacklisted: bool, correct_password: bool, failed_attempts: int) -> bool:
    """
    Determines if a login attempt should be blocked.
    
    A login attempt is blocked if:
    - The IP address is blacklisted OR
    - The password is incorrect AND there have been at least 3 failed attempts
    
    :param ip_blacklisted: Boolean indicating if the IP is blacklisted
    :param correct_password: Boolean indicating if the provided password is correct
    :param failed_attempts: Integer representing the number of failed attempts
    :return: Boolean indicating if the login attempt is blocked
    """
    return ip_blacklisted or (not correct_password and failed_attempts >= 3)
test_cases = [
    (True, True, 0),   
    (True, False, 6),  
    (False, False, 3), 
    (False, False, 1), 
    (False, True, 3),  
]

for ip_blacklisted, correct_password, failed_attempts in test_cases:
    print(is_login_blocked(ip_blacklisted, correct_password, failed_attempts))


#OOP - Classes & Objects
#1. **Bank Account Management:**
 #Create a class `BankAccount` with attributes `owner`, `balance`, and methods `deposit(amount)`
#and `withdraw(amount)`. Ensure the balance never goes negative.

class BankAccount:
    def __init__(self, owner, balance=0.0):
        """Initialize a bank account with owner and balance."""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw a specified amount from the account, ensuring balance does not go negative."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount must be positive.")
    
    def __str__(self):
        """Return a string representation of the bank account."""
        return f"BankAccount(owner={self.owner}, balance=${self.balance:.2f})"
if __name__ == "__main__":
    account = BankAccount("bilal", 2000)
    print(account)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)


#2. **Smartphone Features:**
 #Create a class `Smartphone` with attributes `brand`, `model`, and `battery_level`. Add methods
#`charge()` to increase battery and `use_battery()` to decrease it.

class Smartphone:
    def __init__(self, brand, model, battery_level=100):
        """Initialize the smartphone with brand, model, and battery level."""
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
    
    def charge(self, amount):
        """Increase battery level by the given amount, up to 100%."""
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Battery charged to {self.battery_level}%.")
    
    def use_battery(self, amount):
        """Decrease battery level by the given amount, but not below 0%."""
        if self.battery_level - amount < 0:
            print("Battery is too low! Please charge your phone.")
            self.battery_level = 0
        else:
            self.battery_level -= amount
            print(f"Battery level is now {self.battery_level}%.")
    
    def __str__(self):
        """Return a string representation of the smartphone."""
        return f"{self.brand} {self.model} - Battery: {self.battery_level}%"

phone = Smartphone("Apple", "iPhone 15", 40)
print(phone)
phone.charge(30)
phone.use_battery(60)
print(phone)


#3. **Food Delivery Order:**
# Design a class `Order` that has `customer_name`, `items`, and a method `calculate_total()` to
#return the total bill. Add a method `apply_discount()` if a coupon is used.


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  
    
    def add_item(self, item_name, price):
        self.items.append((item_name, price))
    
    def calculate_total(self):
        return sum(price for _, price in self.items)
    
    def apply_discount(self, discount_percentage):
        total = self.calculate_total()
        discount_amount = total * (discount_percentage / 100)
        return total - discount_amount
    
    def __str__(self):
        item_list = "\n".join([f"{item}: ${price:.2f}" for item, price in self.items])
        return f"Order for {self.customer_name}\nItems:\n{item_list}\nTotal: ${self.calculate_total():.2f}"

order = Order("Tayyaba Altaf")
order.add_item("Burger", 10.99)
order.add_item("Loaded Fries", 3.99)
order.add_item("coldrinks", 1.99)
print(order)
print(f"Total after 20% discount: ${order.apply_discount(20):.2f}")


#4. **Car Rental System:**
 #Create a `Car` class with `model`, `rental_price`, and a method `rent(days)` that calculates the
#total rental cost. Include a method `apply_discount()` for long rentals.

class Car:
    def __init__(self, model, rental_price):
        """
        Initializes a Car object.
        :param model: str - The model of the car.
        :param rental_price: float - The daily rental price of the car.
        """
        self.model = model
        self.rental_price = rental_price

    def rent(self, days):
        """
        Calculates the total rental cost.
        :param days: int - The number of days the car is rented.
        :return: float - The total rental cost after applying any applicable discounts.
        """
        total_cost = self.rental_price * days
        return self.apply_discount(total_cost, days)

    def apply_discount(self, total_cost, days):
        """
        Applies a discount for long-term rentals.
        :param total_cost: float - The initial total rental cost.
        :param days: int - The number of days the car is rented.
        :return: float - The final rental cost after discount.
        """
        if days >= 7:
            return total_cost * 0.9  
        return total_cost

car1 = Car("lamborghini veneco ", 50)
print(f"Total rental cost: ${car1.rent(10):.2f}")  


#5. **Movie Streaming Platform:**
 #Implement a `User` class with `name`, `subscription_type`, and a method `watch_movie(movie)`.
#Only premium users can watch certain movies.

class User:
    def __init__(self, name, subscription_type):
        self.name = name
        self.subscription_type = subscription_type.lower()
    
    def watch_movie(self, movie):
        if movie['premium'] and self.subscription_type != 'premium':
            return f"Sorry, {self.name}. Upgrade to Premium to watch '{movie['title']}'"
        return f"Enjoy watching '{movie['title']}', {self.name}!"

movies = [
    {"title": "Inception", "premium": True},
    {"title": "The Matrix", "premium": False},
]

user1 = User("Mahnoor", "premium")
user2 = User("Yashfa", "basic")

print(user1.watch_movie(movies[0]))  
print(user2.watch_movie(movies[0]))  
print(user2.watch_movie(movies[1]))  



#OOP - Inheritance
#1. **Animal Sound System:**
 #Create a base class `Animal` with a method `make_sound()`. Derive `Dog` and `Cat` classes that
#override `make_sound()` with 'Bark' and 'Meow'.

class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.make_sound()) 
print(cat.make_sound())  



#2. **E-commerce Platform:**
 #Create a base class `Product` with attributes `name` and `price`. Derive `Electronics` and
#`Clothing` classes with additional attributes and methods.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty  # warranty in years

    def get_details(self):
        return f"Electronics: {self.name}, Brand: {self.brand}, Price: ${self.price:.2f}, Warranty: {self.warranty} years"

class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Clothing: {self.name}, Size: {self.size}, Material: {self.material}, Price: ${self.price:.2f}"

electronic_item = Electronics("Laptop", 1200, "HP", 2)
clothing_item = Clothing("T-Shirt", 25, "M", "Cotton")

print(electronic_item.get_details())
print(clothing_item.get_details())


#3. **Online Learning System:**
 #Implement a `Course` class with a `course_name` and method `get_details()`. Create
# `PythonCourse` and `DataScienceCourse` that inherit from `Course`.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
    
    def get_details(self):
        return f"Course Name: {self.course_name}"

class PythonCourse(Course):
    def __init__(self):
        super().__init__("Python Programming")
    
    def get_details(self):
        return f"{super().get_details()} - learn the basics to advanced Python programming."

class DataScienceCourse(Course):
    def __init__(self):
        super().__init__("Data Science")
    
    def get_details(self):
        return f"{super().get_details()} - explore data analysis, machine learning, and AI concepts."

python_course = PythonCourse()
data_science_course = DataScienceCourse()

print(python_course.get_details())
print(data_science_course.get_details())


#4. **Company Employee Management:**
 #Create a base class `Employee` with attributes `name` and `salary`. Derive `Manager` and
#`Developer`, each with an additional attribute.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_info(self):
        return f"{super().display_info()}, Programming Language: {self.programming_language}"

mgr = Manager("mohsin", 80000, "HR")
dev = Developer("hunzla", 60000, "Python")

print(mgr.display_info())
print(dev.display_info())


#5. **Vehicle Types:**
 #Create a `Vehicle` base class. Derive `Car` and `Bike` with an overridden `max_speed()` method.

class Vehicle:
    def max_speed(self):
        raise NotImplementedError("Subclasses must implement max_speed method")

class Car(Vehicle):
    def max_speed(self):
        return "Car max speed: 300 km/h"

class Bike(Vehicle):
    def max_speed(self):
        return "Bike max speed: 200 km/h"

car = Car()
bike = Bike()

print(car.max_speed())  
print(bike.max_speed()) 