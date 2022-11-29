class textfileread():

    def textfielreaddata(self):
        filepathandname="C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\input\\Testdata.txt"
        writefilepath="C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\Output\\outputfile.txt"
        txtfile=open(filepathandname,"r")
        #print(txtfile.read())
        """print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())"""
        """totalrows=txtfile.readlines()
        for eachvalue in totalrows:
            print(eachvalue)
        #txtfile.close()
        ########### Write
        writefile=open(writefilepath,"w")
        #writefile.write("This is sathish from besant technology")
        #writefile.close()"""
        ############ Read and write together
        """writefile = open(writefilepath, "w")
        totalrows = txtfile.readlines()
        for eachvalue in totalrows:
            print(eachvalue)
            writefile.write(eachvalue)
        writefile.close()
        txtfile.close()"""
        appendfile = open(writefilepath, "a")
        appendfile.write("\n This is an append data")
        appendfile.close()




obj=textfileread()
obj.textfielreaddata()