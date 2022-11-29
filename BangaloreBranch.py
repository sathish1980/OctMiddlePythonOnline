from BesantHeadoffice import Besanthedadoffice


class BangaloreBranch(Besanthedadoffice):
    bangaloreAddress = "Bangalore,Karnataka,India"

    def printaddress(self, whichaddress):
        if whichaddress == "branch":
            print(self.bangaloreAddress)
        elif whichaddress == "ho":
            print(self.HOaddress)
        else:
            print("invalid address")

    def discount(self, dicountapplicable):
        if dicountapplicable == True:
            print("You are elgible for dicount of 20%")
        else:
            print("You ar enot eligible for discount percentage")
            print("You have to pay the full amount")

obj=BangaloreBranch()
obj.printaddress("branch")
obj.discount(True)