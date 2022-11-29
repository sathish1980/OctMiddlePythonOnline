from ChennaiBranch import chennaiBranch
from Chennaiofline import chennaiofline


class chennaistudentsporfoli(chennaiBranch,chennaiofline):

    def studenddetails(self):
        print("Python",20)
        print("c#",5)
        print("selenium",25)

    def classmode(self):
        print("online")
        print("Offline")


obj=chennaistudentsporfoli()
obj.printaddress("branch")
obj.courseofferedinHO()
obj.studenddetails()
obj.classmode()
obj.pythoncourseduration()
