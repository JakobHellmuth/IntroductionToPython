import unittest

from vehicle import InvalidVehicleParameters, Vehicle


class TestVehicle(unittest.TestCase):
    def test_valid_vehicle_parameters(self):
        vehicle_parameters = {
            "vehicle_type": "car",
            "mass": 1500,
            "drag_coefficient": 0.31,
            "cross_sectional_area": 1.97,
            "rolling_resistance_coefficient": 0.015,
        }

        vehicle = Vehicle.from_parameters(vehicle_parameters)

        self.assertEqual(vehicle_parameters["vehicle_type"], vehicle.vehicle_type)
        self.assertEqual(vehicle_parameters["mass"], vehicle.mass_kg)
        self.assertEqual(
            vehicle_parameters["drag_coefficient"], vehicle.drag_coefficient
        )
        self.assertEqual(
            vehicle_parameters["cross_sectional_area"], vehicle.cross_sectional_area_m2
        )
        self.assertEqual(
            vehicle_parameters["rolling_resistance_coefficient"],
            vehicle.rolling_resistance_coefficient,
        )

    def test_invalid_parameters(self):
        invalid_vehicle_parameters = {
            "vehicle_typo": "motorcycle",
            "mass": 200,
            "drag_coefficient": 0.57,
            "cross_sectional_area": 0.79,
            "rolling_resistance_coefficient": 0.015,
        }

        self.assertRaises(
            InvalidVehicleParameters,
            Vehicle.from_parameters,
            invalid_vehicle_parameters,
        )


if __name__ == "__main__":
    unittest.main()
