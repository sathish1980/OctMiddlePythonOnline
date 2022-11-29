from Bag.Vehicle import vehicle


class Bike(vehicle):

    def bikename(self):
        print("Yamaha")
        print(self.TyreType)

    def bikeModel(self):
        print("Yamaha R15")

    def bikemakeyear(self):
        print("2022")


obj=Bike()
obj.bikename()
obj.bikeModel()
obj.bikemakeyear()
obj.maxspeed()
obj.colors()