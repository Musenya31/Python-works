# question one 
# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} 🦸‍♂️, and I protect {self.city} using my {self.power}!")

# Derived class (demonstrates inheritance and encapsulation)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)
        self.__flying_speed = flying_speed  # Encapsulated attribute

    def fly(self):
        print(f"{self.name} is flying at {self.__flying_speed} km/h! 🛫")

    def get_speed(self):
        return self.__flying_speed

    def set_speed(self, speed):
        if speed > 0:
            self.__flying_speed = speed
        else:
            print("Speed must be positive!")

# Create objects
hero1 = Superhero("Shadow Blade", "Invisibility", "Night City")
hero2 = FlyingHero("SkyFire", "Flame Wings", "Skyland", 500)

hero1.introduce()
hero2.introduce()
hero2.fly()

#question two 
# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves...")

# Derived classes with polymorphism
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing in the water 🚢")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
