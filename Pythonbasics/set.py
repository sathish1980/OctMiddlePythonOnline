class set():

    def setimplementation(self):
        listfruits = ["apple", "orange", "banana"]
        tuplefruits = ("apple", "orange", "banana", "apple", "cheery")
        setfruits = {"apple", "orange", "banana", "apple", "cheery"}
        print(type(listfruits))
        print(type(tuplefruits))
        print(type(setfruits))
        print(listfruits)
        print(tuplefruits)
        print(setfruits)
        #print(setfruits[0])
        for fruit in setfruits:
            print(fruit)
        setfruits.add("gauva")
        print(setfruits)
        oldsetvalue=setfruits.copy()
        print(oldsetvalue)
        setfruits.clear()
        print(setfruits)
        oldsetvalue.discard("orange")
        print(oldsetvalue)
        oldsetvalue.pop()
        print(oldsetvalue)
        #oldsetvalue.remove("orange")
        print(oldsetvalue)
        print(len(oldsetvalue))
        setseason = {"summer","winter"}
        oldsetvalue.update(setseason)
        oldsetvalue.update("apple")
        print(oldsetvalue)
        course1={"python","selenium","sql","manual","java"}
        course2={"java","selenium","manual","python","devops"}
        print(course1)
        print(course2)
        differenceincourse1=course1.difference(course2)
        print("differnec",differenceincourse1)
        """course1.difference_update(course2)
        print(course1)"""
        intersectioncourse1 = course1.intersection(course2)
        print(intersectioncourse1)
        course1.intersection_update(course2)
        print("course1",course1)
        print("course2",course2)
        print(course1.isdisjoint(course2))
        existornot=course1.issubset(course2)
        print(existornot)

        existornotsuperset = course1.issuperset(course2)
        print(existornotsuperset)
        symtericdifferences = course1.symmetric_difference(course2)
        print(symtericdifferences)

        print(course1)
        print(course2)
        differenceincourse2 = course1.difference(course2)
        print(differenceincourse2)
        course1.symmetric_difference_update(course2)
        print(course1)
        print("course1", course1)
        print("course2", course2)
        print(course1.union(course2))




obj=set()
obj.setimplementation()