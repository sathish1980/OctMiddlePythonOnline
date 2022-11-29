import datetime
class dataandtime():

    def currentdataandtime(self):
        presntdateandtime = datetime.datetime.now()
        print(presntdateandtime)
        print(presntdateandtime.strftime("%x"))

obj=dataandtime()
obj.currentdataandtime()

