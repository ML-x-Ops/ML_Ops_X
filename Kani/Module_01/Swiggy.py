class Hotel:
    def order(self, item):
        raise NotImplementedError("Subclasses must implement this method.")

class Veg_Hotel(Hotel):
    def order(self, item):
        return f"Thank you, your order '{item}' has been placed in The Patiala House."

class Non_Veg_Hotel(Hotel):
    def order(self, item):
        return f"Thank you, your order '{item}' has been placed in Zaitoon."

hotel_map = {
    "veg": Veg_Hotel,
    "non-veg": Non_Veg_Hotel
}

food_type = input("Enter the type of food you need (veg/non-veg): ").lower()
item = input("Enter the food item you want to order: ")

try:
    hotel_class = hotel_map[food_type]()
    print(hotel_class.order(item))
except KeyError:
    print("Sorry, we only support 'veg' or 'non-veg' orders.")
