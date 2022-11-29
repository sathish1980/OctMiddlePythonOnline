class conditions():

    def conditionsimplementation(self,color,vehicle,vehiclecondition):
        if color=="Green" and vehicle!="":
            print("Signal turns as Green")
            print("So You are good to go")
            print("Take care")
        elif color=="Red":
            print("Signal turns as RED")
            print("So You have to wait")
            print("Please Stop")
            if vehicle=="Ambulance" and vehiclecondition =="Full":
                #if vehiclecondition =="Full":
                print("You are Ambulance ,So You are good to go")
                print("Please give a way")
            else:
                print("You have to wait till the signal turn in to green")


        elif color=="Yellow":
            print("Signal turns as Yellow")
            print("you are about to start")
            print("Please start your engine")
        else:
            print("This is a incorrect color")

obj= conditions()
obj.conditionsimplementation("Green","","Full")
