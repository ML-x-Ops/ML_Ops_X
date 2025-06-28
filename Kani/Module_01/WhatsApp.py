class WhatsApp():
    def download(self,file):
        raise NotImplementedError("This module will be executed first")

class Images(WhatsApp):
    def download(self, file):
        return f"Your {file} have been exported successfully."

class Videos(WhatsApp):
    def download(self, file):
        return f"Your {file} have been exported successfully."

class Document(WhatsApp):
    def download(self, file):
        return f"Your {file} have been exported successfully."
    
types = {"img":Images, "vdo":Videos, "doc":Document}

user_input = input("Enter the type of file you need? ").lower()

try:
    download_class = types[user_input]()
    print(download_class.download(user_input))
except KeyError:
    print("Musy be an valid one")