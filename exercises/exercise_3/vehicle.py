KILOMETERS_PER_HOUR_TO_METERS_PER_SECOND = 3.6
GRAVITY_CONSTANT = 9.81  # not stricly necessary to define a constant here


class Vehicle:
    def __init__(
        self,
        brand,
        model,
        mass_kg,
        drag_coefficient,
        cross_sectional_area_m2,
        rolling_resistance_coefficient,
    ):
        self.brand = brand
        self.model = model
        self.mass_kg = mass_kg
        self.drag_coefficient = drag_coefficient
        self.cross_sectional_area_m2 = cross_sectional_area_m2
        self.rolling_resistance_coefficient = rolling_resistance_coefficient

    def calc_power_consumption(self, speed_kph, air_density_kg_per_m3):
        air_resistance_power = (
            0.5
            * air_density_kg_per_m3
            * (speed_kph / KILOMETERS_PER_HOUR_TO_METERS_PER_SECOND) ** 3
            * self.drag_coefficient
            * self.cross_sectional_area_m2
        )

        rolling_resistance_power = (
            self.rolling_resistance_coefficient
            * self.mass_kg
            * GRAVITY_CONSTANT
            * (speed_kph / KILOMETERS_PER_HOUR_TO_METERS_PER_SECOND)
        )
        power_consumption = air_resistance_power + rolling_resistance_power

        return power_consumption

    def change_tyre(self, new_rolling_resistance_coefficient):
        self.rolling_resistance_coefficient = new_rolling_resistance_coefficient
