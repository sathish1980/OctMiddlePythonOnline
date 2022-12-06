import csv

class csvfilereadandwrite():

    def csvfileread(self):
        filepath="C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\input\\Testdata.csv"
        with open(filepath, mode='r') as csvreaddata:
            # reading the CSV file
            csvFile = csv.reader(csvreaddata) #return the list of data

            # displaying the contents of the CSV file
            for lines in csvFile:
                print(lines)
                for eachcolumvalue in lines:
                    print(eachcolumvalue)

    def csvwrite(self):
        fields = ['Name', 'Branch', 'Year', 'CGPA']

        # data rows of csv file
        rows = [['Nikhil', 'COE', '2', '9.0'],
                ['Sanchit', 'COE', '2', '9.1'],
                ['Aditya', 'IT', '2', '9.3'],
                ['Sagar', 'SE', '1', '9.5'],
                ['Prateek', 'MCE', '3', '7.8'],
                ['Sahil', 'EP', '2', '9.1']]

        # name of csv file
        filename = "C:\\Users\\sathishkumar\\PycharmProjects\\OctMiddlePythonOnline\\Output\\outputfile.csv"

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)
obj=csvfilereadandwrite()
obj.csvwrite()