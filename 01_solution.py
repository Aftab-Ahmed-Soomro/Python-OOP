class Car:
    total_cars = 0
    
    # Special Constructor
    def __init__(self, brand, model):
        # private
        self.__brand = brand
        self.__model = model
        # self.total_cars + = 1
        Car.total_cars += 1
        
    # encapsulate
    def get_brand(self):
        return self.__brand + " !"    
    
    # setter
    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and len(new_brand.strip()) > 0:
            self.__brand = new_brand
            print(f"Brand successfully update ho kar '{new_brand}' ban gaya.")
        else:
            print("Invalid brand! Brand aik non-empty text hona chahiye.")    
        
    # Method/ function 
    def Specs(self):
        return f"Car is specially designed as {self.__brand} with features of {self.__model}"
    
    # polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    # polymorphism
    def fuel_type(self):
        return "Electric Charge"    
    
# my_car = Car("Toyota", "Corolla")

# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

# specs = Car("Tata", "Safari")

# print(specs.Specs())

# my_tesla = ElectricCar("Tesla", "Model S", "85kWH")

# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.Specs())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())
# my_tesla.set_brand("")
# my_tesla.set_brand("Honda")

# print(Car.total_cars)
# print(Car.general_description())

# print(my_car.model)

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# Multiple Inheritence
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass
    
my_new_tesla = ElectricCarTwo("Tesla", "Model S")    
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())