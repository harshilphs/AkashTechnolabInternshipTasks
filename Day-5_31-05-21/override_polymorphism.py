class Car:
    def brand(self):
        print("This is car")

class Tesla(Car):
    #override
    def brand(self):
        print("This is Tesla")

obj = Tesla()
obj.brand()