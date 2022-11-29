print("sathish")
#print('sathish')
"""print(34)
print("sathish\n","kumar",55)
print("sathish's")"""
print("""Besant is the best "Training" institute""")
print("""This is sathish kumar
I an a software testing trainer
i am expertise in selenium""")
age=3.45
print(type(age))


def add(): # function
    print("addition of 2 number is:")  #function implementation


add() #function call

#function wihout parameter /arguments
def addition():
    a=10
    b=20
    c=a+b
    print("addition of 2 number is:",c)
#function with parameter/ arguments
def subtraction(a,b):
    c=a-b
    d=mul()
    print("subtraction of 2 number: ",c)
    print("The multiplication of 2 number is :", d)
#function without return type

#function with return type
def mul():
    a=3
    b=5
    c=a*b
    print("The multiplication of 2 number is :", c)
    return c

def age(birthyear):
    currentyear=2022
    actualage=currentyear-birthyear
    return actualage

def validateyouthornot(birthyear):
    agevalue=age(birthyear)
    if agevalue>18:
        print("you are youth")


addition()
subtraction(5,8)
validateyouthornot(1990)
