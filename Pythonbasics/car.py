from Pythonbasics.Vehicle import vehicle


class car(vehicle):
    def carname(self):
        print("suzuki")
    def speed(self,speed):
        print("max speed is", speed)


obj =car()
obj.carname()
obj.speed(200)
#obj1=vehicle()
#obj1.speed()
obj.change_gear()