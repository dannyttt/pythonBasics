# making a nobject from a class is called instantiation
# and you work with instances of a class.
class Dog:
    """A sunoke attenot ti nidek a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} rolled over')


my_dog = Dog('Lucky', 5)
print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()

# default value


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        print(
            f'make: {self.make} model: {self.model} year: {self.year}')

    def read_odometer(self):
        print(self.odometer_reading)

    # method
    def drive_car(self, milage):
        self.odometer_reading += milage


acura = Car('Acura', 'RDX', 2022)
acura.get_descriptive()
acura.drive_car(10)
acura.drive_car(10)
acura.read_odometer()

# inheritance
# use super() allows to call from the parent method


class Batter:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'{self.battery_size}-KWh battery')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_percentage = 0
        self.battery = Batter(100)
    # definning attributes and method for the child class

    def charge_battery(self, percentage):
        if self.battery_percentage + percentage > 100:
            self.battery_percentage = 100
        else:
            self.battery_percentage += percentage

    def drive_electic(self, milage):
        self.odometer_reading += milage
        self.battery_percentage -= milage/2

    def battery_usage(self):
        print(self.battery_percentage)


tesla = ElectricCar('tesla', 'model-X', 2022)
tesla.get_descriptive()
tesla.drive_electic(30)
tesla.charge_battery(100)
tesla.read_odometer()
tesla.battery_usage()
tesla.battery.describe_battery()
