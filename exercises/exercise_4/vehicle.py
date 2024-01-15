# basically the same as for exercise 3, but added a classmethod
# for initialization from parameters

KILOMETERS_PER_HOUR_TO_METERS_PER_SECOND = 3.6
GRAVITY_CONSTANT = 9.81  # not stricly necessary to define a constant here


class InvalidVehicleParameters(Exception):
    pass


class Vehicle:
    def __init__(
        self,
        vehicle_type,
        mass,
        drag_coefficient,
        cross_sectional_area,
        rolling_resistance_coefficient,
    ):
        self.vehicle_type = vehicle_type
        self.mass_kg = mass
        self.drag_coefficient = drag_coefficient
        self.cross_sectional_area_m2 = cross_sectional_area
        self.rolling_resistance_coefficient = rolling_resistance_coefficient

    @classmethod
    def from_parameters(cls, vehicle_parameters):
        allowed_attributes = [
            "vehicle_type",
            "mass",
            "drag_coefficient",
            "cross_sectional_area",
            "rolling_resistance_coefficient",
        ]
        valid_parameters = {
            key: value
            for key, value in vehicle_parameters.items()
            if key in allowed_attributes
        }
        if vehicle_parameters != valid_parameters:
            raise InvalidVehicleParameters("Invalid vehicle parameters obtained.")

        return cls(**vehicle_parameters)

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
