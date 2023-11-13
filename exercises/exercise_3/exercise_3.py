
class Vehicle:
    def __init__(self, brand, mass, dc, rrc, v, cs, p):
        self.brand = brand
        self.mass = mass
        self.dc = dc
        self.rrc = rrc
        self.v = v
        self.cs = cs
        self.p = p
        

    def calculate_power_consumption(self):
        air_resistance_power = (
            0.5
            *self.p
            * self.dc
            * self.cs
            * self.v / 3.6
        )

        rolling_resistance_power = (
            self.rrc
            * self.mass
            * 9.81
            * (self.v / 3.6)
        )

        required_power = (air_resistance_power + rolling_resistance_power) / 1000
    
    def energy_efficiency(self):
        if required_power == 0:
            

        return required_power

bmw = Vehicle("BMW", 2000, 0.9, 0.415, 80, 30, 1.205)
audi = Vehicle("Audi", 1300, 0.41, 0.018, 85, 1.61, 1.205)

bmw_power = bmw.calculate_power_consumption()
audi_power = audi.calculate_power_consumption()

print("BMW power:", bmw_power, end="")
print("[kW]")
print("Audi power:", audi_power, end="")
print("[kW]")




    


