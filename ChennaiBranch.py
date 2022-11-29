from BesantHeadoffice import Besanthedadoffice


class chennaiBranch(Besanthedadoffice):

    chennaiAddress="Chennai,Tamilnadu,India"

    def printaddress(self,whichaddress):
        if whichaddress=="branch":
            print(self.chennaiAddress)
        elif whichaddress=="ho":
            print(self.HOaddress)
        else:
            print("invalid address")
    def discount(self,dicountapplicable):
        if dicountapplicable==True:
            print("You are elgible for dicount of 20%")
        else:
            print("You ar enot eligible for discount percentage")
            print("You have to pay the full amount")


che=chennaiBranch()
che.printaddress("ho")
che.courseofferedinHO()
che.CourseFeeinHO("python")
che.discount(False)