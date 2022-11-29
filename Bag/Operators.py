class  operators():

    def arthimetic(self,a,b):

        print(a+b)
        print(a - b)
        print(a * b)
        print(a / b)
        print(a % b)
        print(a // b)

    def assignement(self):
        a=10
        a+=6 # a=a+2 =12
        print(a)
       # a=+2
        print(a)
        a-=2
        print(a)

    def comparision(self):
        a=11
        b=10
        print(a==b)
        print(a != b)
        print(not(a > b and (a==10 or a<b)))

    def identity(self):
        name="sathish"
        lname="sathish kumar"
        print(name is not lname)

    def membership(self):
        fruits=["apple","orange","banana","grapes"]
        name="sathish"
        lname="kumar sathsh"
        print(name in lname)
        print("banana" not in fruits)

obj=operators()
#obj.arthimetic(10,2)
obj.assignement()
obj.comparision()
obj.membership()
