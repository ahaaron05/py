class Car:
    """Simple model of a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.miles = 0
    
    def get_description(self):
        return  f"Make:\t{self.make}\nModel:\t{self.model}\nYear:\t{self.year}"
    
    def read_odometer(self):
        print(f"Car has {self.miles} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.miles:
            self.miles = mileage
        else: print("You can't roll back the odometer!")

    def incriment_odometer(self, miles):
        if miles >= 0:
            self.miles += miles
        else: print("You can't roll back the odometer!")
    
class Electric_Car(Car):
    """A model of an electric car based off the Car model"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 80
    
    def get_description(self):
        return f"Make:\t{self.make}\nModel:\t{self.model}\nYear:\t{self.year}\nBattery Size:\t{self.battery_size}"
    

car1 = Electric_Car("Tesla", "Model T", 2021)
print(car1.get_description())