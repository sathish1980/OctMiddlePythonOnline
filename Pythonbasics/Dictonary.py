class dictonary():

    def dictonaryimplementaion(self):
        praveen={"STD":"12th","Grade":"A","Available":"30","Grade":"B"}
        print(praveen)
        print(type(praveen))
        print(praveen.get("Grade"))
        print(praveen.get("STDS"))
        print(praveen.keys())
        for eachvalue in praveen.keys():
            print(praveen.get(eachvalue))
        print(praveen.values())
        print(praveen.items())
        for eachval in praveen.items():
            print(eachval)
        #praveen.pop("grader")
        praveen.popitem()
        print(praveen)
        praveen["Available"]="29"
        praveen["Grade"] = "C"
        print(praveen)
        praveen.update({"Grade":"D"})
        print(praveen)
        praveen.setdefault("Grade", "E")
        praveen.setdefault("Exam","2oth Dec")
        print(praveen)
        print(len(praveen))
        copyfun=praveen.copy()
        print(copyfun)
        praveen.clear()
        print(praveen)
        del praveen
        print(praveen)

obj=dictonary()
obj.dictonaryimplementaion()