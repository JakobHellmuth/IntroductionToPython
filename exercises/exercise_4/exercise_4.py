"""Calculates power consumption of multiple vehicles.

Note:
    This is just one potential solution. Of course 
    there are other possible solutions.
    Most important points here are IMO using the 
    standard library to get all json files, proper
    error handling and adding a test to cover this bug.
    
"""
import json
import logging
from pathlib import Path

from vehicle import InvalidVehicleParameters, Vehicle

logger = logging.getLogger("exercise_4")

ENERGY_EFFICIENCY_THRESHOLD_WATTS = 10_000


def check_power_consumption(power_consumption):
    if power_consumption < ENERGY_EFFICIENCY_THRESHOLD_WATTS:
        print("Vehicle is energy-efficient")
    else:
        print("Vehicle is not energy-efficient")


def _get_vehicle_parameter_filepaths(directory_path):
    return directory_path.glob("*.json")


if __name__ == "__main__":
    vehicles = []

    # use pathlib or os instead of hard-coded paths
    directory_path = Path(__file__).parent
    vehicle_parameter_filepaths = _get_vehicle_parameter_filepaths(directory_path)

    for parameter_filepath in vehicle_parameter_filepaths:
        with open(parameter_filepath, mode="r") as file:
            vehicles_data = json.load(file)

        for vehicle_parameters in vehicles_data:
            try:
                vehicle = Vehicle.from_parameters(vehicle_parameters)
            except InvalidVehicleParameters:
                logger.warning(
                    "Invalid vehicle parameters obtained. The vehicle parameters are not used. "
                    f"Please check the vehicle parameters: {vehicle_parameters}"
                )
            else:
                vehicles.append(vehicle)

    for vehicle in vehicles:
        power_consumption = vehicle.calc_power_consumption(
            speed_kph=80, air_density_kg_per_m3=1.204
        )
        check_power_consumption(power_consumption)
