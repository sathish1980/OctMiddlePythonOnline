class stringconcpets():

    def stringconceptimplementation(self):
        name = ' sathish kumar R B.tech '
        name3= "  "
        print(name)
        print(name[1]) # to get he character based on position
        print(name[1:6])
        print(name[-1])
        print(len(name)) # to get the total character count
        totallength=len(name)
        for each in range(0,totallength):
            print(name[each])
        #or
        for charc in name:
            print(charc)
        exist= "kumar" not in name
        print(exist)
        if exist :
            print("The given search txt is avaialble in the string")
        else:
            print("this is not avaialble")
        print(name.upper())
        print(name.lower())
        #print(name.strip())
        print(name.lstrip())
        print(name.rstrip())
        print(name.replace(" ",""))
        print(name.replace("ath","A"))
        print(name.split("a"))
        print(name.split(" "))
        aftersplit=name.split(" ")

        print(type(aftersplit))
        print(name.startswith(" Sathis"))
        print(name.endswith(" "))
        print(name.__contains__("kum"))
        print(name.count("a"))
        name1 ="besant"
        print(name.join(name1))
        print(name+name1)
        print(name.find("a"))
        print(name.rfind("a"))
        filename="sathis.txt"
        filesperator=filename.find(".")
        print(filesperator)
        print(len(filename))
        actualfilename=filename[filesperator+1:len(filename)]
        print(actualfilename)
        if actualfilename == "txt":
            print("this is txt file")
        elif actualfilename == "xlsx" or actualfilename == "xls":
            print("this is excel file")
        elif actualfilename == "xml":
            print("this is xml file")
        print(name.isnumeric())
        print(name.isalpha())
        print(filename.index("."))
        print(name3.isspace())
        print(name)






obj=stringconcpets()
obj.stringconceptimplementation()