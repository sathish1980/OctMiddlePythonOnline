class conditionimplementations():

    def ifcondition(self,color,vehicle,patieninornot):
        if color == "Red":
            if vehicle=="Ambulance" and patieninornot=="Yes":
                print("Please give a way for ambulance")
            else:
                print("You have to stop")
                print("Dont blow a horn")
                print("You have to wait for next 60 min")
        elif color == "Green":
            print("You are good to go")
        elif color == "Yellow":
            print("you are about to start")
        else:
            print("This is not a valid color")

    def gender(self,Gender):
        if Gender=="Male":
            pass

obj =conditionimplementations()
obj.ifcondition("Red","Bike","Yes")