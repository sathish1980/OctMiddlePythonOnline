from Pythonbasics.Ferrari import ferrari


class BMW():

    def name(self):
        print("This is BMW")

    def model(self):
        print("2000seirs")

obj1=BMW()
obj2=ferrari()

for eachvalue in (obj1,obj2):
    eachvalue.name()
    eachvalue.model()
