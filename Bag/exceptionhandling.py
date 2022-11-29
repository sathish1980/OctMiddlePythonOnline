class exceptionhandling():

    def add(self,a,b):
        try:
            c=a+b
            print(c)
        except:
            print("error")

    def div(self,a,b):
        try:
            c=a/b
            print(c)
        except ZeroDivisionError:
            print("Hey you have entered zero value")
        except:
            print("Hey you got an error")
        finally:
            print("this is final block")
            print("you have enterd a value",a)
            print("you have enterd a value", b)
            print(a+b)


obj=exceptionhandling()
obj.div(12,"")
obj.add(2,3)