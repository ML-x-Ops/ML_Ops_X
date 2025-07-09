class CelsiusSensor:
    def get_temperature(self):
        print("25 degrees Celsius")

class FahrenheitSensor:
    def get_temp_fahrenheit(self):
        print("77 degrees Fahrenheit")

class CelsiusAdapter:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def current_temp(self):
        self.celsius.get_temperature()
    
class FahrenheitAdapter:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
    
    def current_temp(self):
        self.fahrenheit.get_temp_fahrenheit()
    
cel_sen = CelsiusSensor()
fah_sen = FahrenheitSensor()

cel_adp = CelsiusAdapter(cel_sen)
fah_adp = FahrenheitAdapter(fah_sen)

cel_adp.current_temp()
fah_adp.current_temp()