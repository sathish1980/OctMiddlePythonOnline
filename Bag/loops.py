class loops():

    def whileloops(self,intialvalue):
        next10digit=intialvalue+10
        while(intialvalue<=next10digit):
            intialvalue+=1 # intialvalue =intialvalue+1
            if intialvalue==15:
                continue
            print(intialvalue)

    def whileloopsinreverse(self,intialvalue):
        next10digit=intialvalue-10
        while(intialvalue>=next10digit):
            print(intialvalue)
            intialvalue-=1 # intialvalue =intialvalue+1
            if intialvalue==15:
                break

    def forloops(self):
        fruits=["apple","orange","banana","grapes"]
        for eachvalue in fruits:
            if eachvalue== "banana":
                continue
            print(eachvalue)

        for eachvalue in range(2,10):
            print(eachvalue)

obj= loops()
obj.forloops()
