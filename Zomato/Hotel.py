class Hotel():

    VegHotelName={"SVB":"Saravanabhavan ,chennai","A2B":"Adhayaranadha bhavan , chennai","PSB":"punjab hotel ,kerala"}
    nonVegHotelName = {"SVB": "Saravanabhavan ,chennai", "A2B": "Adhayaranadha bhavan , chennai",
                    "PSB": "punjab hotel ,kerala"}
    identified=False
    def Hoteladdress(self,HotelKey):
        for  eachhotelkey in self.VegHotelName.keys():
            if eachhotelkey == HotelKey:
                print(self.VegHotelName.get(eachhotelkey))
                self.identified = True
                break
        if self.identified==True:
            pass
        else:
            print(HotelKey,"With the given Hotel key i dont find anything near by")


