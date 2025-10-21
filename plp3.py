# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}, and I wield the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass with encapsulation and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.__flight_speed = flight_speed  

    def use_power(self):
        return f"{self.name} soars through the sky at {self.__flight_speed} km/h using {self.power}!"

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.gadgets = gadgets

    def use_power(self):
        return f"{self.name} deploys {', '.join(self.gadgets)} to amplify {self.power}!"

hero_name = input("Enter your hero's name: ")
hero_power = input("Enter your hero's power: ")
hero_origin = input("Enter your hero's origin: ")


hero = Superhero(hero_name, hero_power, hero_origin)

# Call methods
print(hero.introduce())
print(hero.use_power())




class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        return "Driving on the road "

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky "

class Boat(Vehicle):
    def move(self):
        return "Sailing across the sea "

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling on the path "

# Polymorphic behavior
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())


