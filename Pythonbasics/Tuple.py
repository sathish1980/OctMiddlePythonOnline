class tuple():

    def tupleimplementation(self):
        listfruits=["apple","orange","banana"]
        tuplefruits=("apple","orange","banana","apple","cheery")
        print(type(listfruits))
        print(type(tuplefruits))
        print(tuplefruits.count("apple"))
        print(tuplefruits.index("apple"))
        print(len(tuplefruits))
        print(tuplefruits[0])
        print(tuplefruits[1:3])
        print(tuplefruits[-1])
        for eachfruit in tuplefruits:
            print(eachfruit)
        #tuplefruits[1]="grapes"
        print(tuplefruits)
        converttupleintoList=list(tuplefruits)
        print(type(converttupleintoList))
        #converttupleintoList[1]="grapes"
        print(converttupleintoList)
        #newtuple=tuple(converttupleintoList)
        #print(newtuple)
        tuplefruitsrare = ("durian","mangoosethan")
        tuplefruits+=tuplefruitsrare
        print(tuplefruits)
        #del tuplefruits
        print(tuplefruits)



obj=tuple()
obj.tupleimplementation()