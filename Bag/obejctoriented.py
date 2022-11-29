class objectoriented():
    print("sathish")
    global c
    c=50
    a = 100 #global variable
    username,firstname,lastname="sathish","kumar","sathish189"
    apple=banana=orange=30
    apple=30
    banana=30
    orange=30
    name="sathish's"

    def add_two_numner(self,a,b):
        print(a+b)

    def add(self,e,f,g):
        print(e-f)

    def sub(self):
        a = 10 #local variable
        print(a)

# constructor with out parameter
    def __init__(self):
        print(self.a)
        print("This is constuctor eith out parameter")
        print(2+3)

#constructor with parameter
    def __init__(abcd,a,b):
        print(abcd.a)
        print("This is constuctor")
        print(a+b)
        print("Global variable",c)
        print("Global",abcd.username)
        print("Global", abcd.orange)

name=objectoriented(5,9)
#name.add(2,3)
name.sub()


