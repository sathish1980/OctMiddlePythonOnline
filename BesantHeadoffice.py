class Besanthedadoffice():

    HOaddress="Bangalore,Karnataka"
    Course =["python","selenium","java","C#","Azure"]
    Coursefee={"python":20000,"selenium":17000,"java":25000,"C#":30000,"Azure":40000}

    def courseofferedinHO(self):
        for eachCourse in self.Course:
            print(eachCourse)

    def CourseFeeinHO(self,coursename):
        amount=self.Coursefee.get(coursename)
        print("Amount for the selected course",coursename, "is : ",amount)

