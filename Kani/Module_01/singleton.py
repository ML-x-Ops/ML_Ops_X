class SchoolBell:
# Private class variable to hold single instance
    _instance = None #x00000163886CCCD0> / 0x0000025C3D6FCCD0>
# Special method to control instance creation
    def __new__(self):
# Create instance only if doesn’t exist
        if self._instance is None:
            self._instance = super().__new__(self)
            print(self._instance)
        return self._instance
    def ring(self):
        print(" Ringing... Lunch break!")

# bell_a = SchoolBell()
bell_b = SchoolBell()
# Check if they’re same object
# print(bell_a is bell_b) # Output: True
# Both will ring the SAME bell
# bell_a.ring()
bell_b.ring()