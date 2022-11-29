class list():

    def listimplementation(self):
        name="sathish"
        print(name)
        fruits=["apple","orange","banana","apple"]
        print(fruits)
        for each in fruits:
            print(each)
        fruits.append("pineapple")
        print(fruits)
        oldfruits=fruits.copy()
        fruits.clear()
        print(fruits)
        print(oldfruits)
        print(oldfruits.count("plums"))
        veg=["potato","brimjal","drumstick"]
        oldfruits.extend(veg)
        print(oldfruits)
        print(oldfruits.index("banana"))
        oldfruits.insert(22,"cherry")
        print(oldfruits)
        oldfruits.remove("apple")
        print(oldfruits)
        oldfruits.pop(2)
        print(oldfruits)
        oldfruits.pop()
        print(oldfruits)
        oldfruits.pop(2)
        print(oldfruits)
        oldfruits.reverse()
        print(oldfruits)
        oldfruits.sort()
        print(oldfruits)
        oldfruits.sort(reverse=True)
        print(oldfruits)
        print(len(oldfruits))
        print(oldfruits[0:3])
        print(oldfruits[-1])
        oldfruits[1:7]=["Watermelon","raddish","cocunut"]

        print(oldfruits)
        del oldfruits
        print(oldfruits)



obj=list()
obj.listimplementation()