import unittest

from converter import convert_value


class ConvertValueTests(unittest.TestCase):
    def test_length_conversion(self):
        self.assertAlmostEqual(
            convert_value(2, "Length", "Kilometers (km)", "Meters (m)"), 2000
        )

    def test_mass_conversion(self):
        self.assertAlmostEqual(
            convert_value(1, "Mass", "Kilograms (kg)", "Pounds (lb)"), 2.20462262
        )

    def test_volume_conversion(self):
        self.assertAlmostEqual(
            convert_value(1, "Volume", "Liters (L)", "Milliliters (mL)"), 1000
        )

    def test_area_conversion(self):
        self.assertAlmostEqual(
            convert_value(1, "Area", "Square meters (m²)", "Square centimeters (cm²)"),
            10000,
        )

    def test_temperature_conversion(self):
        self.assertAlmostEqual(
            convert_value(32, "Temperature", "Fahrenheit (°F)", "Celsius (°C)"), 0
        )

    def test_rejects_units_from_another_category(self):
        with self.assertRaises(ValueError):
            convert_value(1, "Length", "Pounds (lb)", "Meters (m)")


if __name__ == "__main__":
    unittest.main()
