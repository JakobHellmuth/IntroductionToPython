"""Calculates power consumption of multiple vehicles.

Note:
    This is just one potential solution. Of course 
    there are other possible solutions.
    
"""
from vehicle import Vehicle

ENERGY_EFFICIENCY_THRESHOLD_WATTS = 10_000


def check_power_consumption(power_consumption):
    if power_consumption < ENERGY_EFFICIENCY_THRESHOLD_WATTS:
        print("Vehicle is energy-efficient")
    else:
        print("Vehicle is not energy-efficient")


if __name__ == "__main__":
    vehicle = Vehicle(
        brand="Ford",
        model="Fusion",
        mass_kg=1500,
        drag_coefficient=0.31,
        cross_sectional_area_m2=1.97,
        rolling_resistance_coefficient=0.015,
    )

    power_consumption = vehicle.calc_power_consumption(
        speed_kph=80, air_density_kg_per_m3=1.204
    )
    check_power_consumption(power_consumption)

    vehicle.change_tyre(new_rolling_resistance_coefficient=0.02)
    power_consumption_after_tyre_change = vehicle.calc_power_consumption(
        speed_kph=80, air_density_kg_per_m3=1.204
    )
    check_power_consumption(power_consumption_after_tyre_change)
