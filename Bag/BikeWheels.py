from Bag.Bike import Bike
from Bag.RBI import RBI
from Bag.SBI import SBI


class BikeWheels(Bike,RBI,SBI):

    def BikeWheelType(self):
        print("Alloy wheel")
        print("Spoke wheel")

    def TyreMM(self):
        print("120MM")
        print("10MM")

obj=BikeWheels()
obj.TyreMM()
obj.BikeWheelType()
obj.bikename()
obj.bikeModel()
obj.maxspeed()
obj.colors()