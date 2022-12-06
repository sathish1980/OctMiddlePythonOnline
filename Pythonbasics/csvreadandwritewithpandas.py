import pandas
class csvreadandwriteusingpandas():

    def csvread(self):
        filepath="C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\input\\Testdata.csv"
        fileouptut="C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\Output\\Testdataoutput03122022.csv"
        csvFile = pandas.read_csv(filepath)
        # displaying the contents of the CSV file
        print(csvFile.head())

        # csvdata=pandas.DataFrame(csvFile,columns=["Name","dob","gender","age","status"])
        csvdata = pandas.DataFrame(csvFile)
        print(csvdata)
        csvdata.to_csv(fileouptut, header=True)
obj=csvreadandwriteusingpandas()
obj.csvread()