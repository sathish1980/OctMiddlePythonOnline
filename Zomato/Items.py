from Zomato.Hotel import Hotel


class Items(Hotel):

    VegItem=["Idly","pongal","poori"]
    nonvegItem=["chiken","mutton","pork"]
    VegItemavaible=False
    NonvegItemavailable=False
    def ItemAvaialble(self,requestedItem):
        for eachvalueinveg in self.VegItem:
            if eachvalueinveg == requestedItem:
                print("The given item",requestedItem,"is available")
                self.VegItemavaible=True

        for eachvalueinnonvag in self.nonvegItem:
            if eachvalueinnonvag == requestedItem:
                print("The given item", requestedItem, "is available")
                self.NonvegItemavailable = True

        if self.VegItemavaible == False and self.NonvegItemavailable == False:
            print(" The given dish",requestedItem, "is not avaialble now")


obj=Items()

obj.Hoteladdress("A2B")
obj.ItemAvaialble("masaldosa")