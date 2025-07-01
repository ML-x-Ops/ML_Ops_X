class ProjecterInterface(): # A3 -> device -> ProjecterInterface()
    def connect(self):      # -> it should have a "connect" method. / rule book like connect is Must.
        pass

class OldLaptop(): # -> This is my old shit laptop which dont have an usb port.
    def output_hdmi(self):
        print("I am old laptop and i was able to send only in HDMI.")

class HdmiToUsbcAdapter(ProjecterInterface): # A4 -> ProjecterInterface()
    def __init__(self,laptop):
        self.laptop = laptop

    def connect(self): # A5 -> Connect
        print("Hello I am Adapter now I can able to connect the HDMI to USB")
        self.laptop.output_hdmi() #kani hdmi

class NewProjecter():
    def connect_device(self, device:ProjecterInterface): #A2 -> device
        print("Projecter connected !")
        device.connect() # A1 -> device # preetha usb

laptop = OldLaptop()
adapter = HdmiToUsbcAdapter(laptop) 
projector = NewProjecter()

projector.connect_device(adapter) 
