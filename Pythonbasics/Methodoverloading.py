class methodoverloading():

    name="sathish kumar"
    name1 ='sathish'

    def add(self,a,b):
        c=a+b
        print("addition",c)

    def add(self,a,b,c,d): #method overloading
        e=a+b+c+d
        print(e)

obj=methodoverloading()
obj.add(2,3,4)