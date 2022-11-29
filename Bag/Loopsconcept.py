class loopsconcept():

    def div(self,a,b):
        try:
            c=a/b
            print(c)
        except ZeroDivisionError:
            print("This is not a valid division number")
        except:
            print("This is error")
        finally:
            print("this is finally")

    def whileloop(self,intialValue):
        try:
            next10digitvale=intialValue+10
            next10digitvalereverse = intialValue - 10
        except:
            print("Exception")

        while (intialValue >= next10digitvalereverse):
            intialValue -= 1
            if intialValue==20:
                continue
            print(intialValue)

    def forloop(abcd):
        a =10
        print(a)
        fruits=["apple","orange","banana","grapes"]
        print(fruits)
        for singlevalue in fruits:
            print(singlevalue)
            if singlevalue=="banana":
                break

        for eachval in range(1,15):
            print(eachval)

    def multiforloop(self):
        try:
            items=[1,2,3,4]
            fruits = ["apple", "orange", "banana", "grapes"]
            for firstloop in items:
                print(firstloop)
                for secondloop in fruits:
                    print(secondloop)
        except:
            print("error")
a=range(1,5) #[1,2,3,4]
print(a)

obj = loopsconcept()
obj.div(2,0)
obj.whileloop(25)
obj.forloop()
obj.multiforloop()
