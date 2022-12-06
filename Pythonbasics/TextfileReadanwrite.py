import time


class textfileread():

    def textfielreaddata(self):
        filepathandname="C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\input\\Testdata.txt"
        writefilepath="C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\Output\\newtext.txt"
        txtfile=open(filepathandname,"r") #r,w,a
        #print(txtfile.read(10))
        """print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())
        print(txtfile.readline())
        totalrows=txtfile.readlines()
        for eachvalue in totalrows:
            print(eachvalue)
            time.sleep(1)
        txtfile.close()
            ########### Write
        writefile = open(writefilepath, "w")
        writefile.write("This is sathish from besant technology")
        writefile.close()
        ############ Read and write together
        writefile = open(writefilepath, "w")
        totalrows = txtfile.readlines()
        for eachvalue in totalrows:
            print(eachvalue)
            writefile.write(eachvalue)
        writefile.close()
        txtfile.close()"""
        appendfile = open(writefilepath, "r")
        appendfile.write("\n This is an append data from sathish")
        appendfile.close()




obj=textfileread()
obj.textfielreaddata()