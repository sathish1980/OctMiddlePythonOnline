import pandas as pd
class excelfilereadandwrirte():

    inputfile ="C:\\Users\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\input\\Testdata.xlsx"
    outputfile = "C:\\Users\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\output\\output.xlsx"
    def excelfilereadandwrite(self):
        df = pd.read_excel(self.inputfile, sheet_name='Input')
        df.head()
        print(df)
        exldata = pd.DataFrame(df)
        print(exldata)
        exldata.to_excel(self.outputfile)

obj=excelfilereadandwrirte()
obj.excelfilereadandwrite()