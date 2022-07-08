#Polymorphism Payment driverless car

class Car:
    
    def __init__(self, name, branch, km, price):
        self.name = name
        self.branch = branch
        self.price = price
        self.km = km

    def __str__(self):
        return 'Car: ' + self.name + ', Branch: ' + self.branch

    def distance(self):
        distance = self.price * self.km
        return str(distance)

    def payment(self):
        return 'Distance: ' + str(self.km) + '\nYou must pay ' + self.distance() + ' Euro for the trip\n'

class Mercedes(Car):
    
    def __init__(self, km, price=2):
        super().__init__('EQS', 'Mercedes-Benz', km, price)

class VW(Car):
    
    def __init__(self, km, price=1):
        super().__init__('Passat', 'VW', km, price)

m = Mercedes(5)
vw = VW(10)

print(m)
print(m.payment())
print(vw)
print(vw.payment())
