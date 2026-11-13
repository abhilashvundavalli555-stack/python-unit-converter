"""Unit conversion logic for the web app."""

UNIT_FACTORS = {
    "Length": {
        "Meters (m)": 1,
        "Kilometers (km)": 1000,
        "Centimeters (cm)": 0.01,
        "Millimeters (mm)": 0.001,
        "Miles (mi)": 1609.344,
        "Yards (yd)": 0.9144,
        "Feet (ft)": 0.3048,
        "Inches (in)": 0.0254,
    },
    "Mass": {
        "Kilograms (kg)": 1,
        "Grams (g)": 0.001,
        "Milligrams (mg)": 0.000001,
        "Pounds (lb)": 0.45359237,
        "Ounces (oz)": 0.028349523125,
    },
    "Volume": {
        "Liters (L)": 1,
        "Milliliters (mL)": 0.001,
        "Cubic meters (m³)": 1000,
        "US gallons (gal)": 3.785411784,
        "US cups (cup)": 0.2365882365,
    },
    "Area": {
        "Square meters (m²)": 1,
        "Square kilometers (km²)": 1_000_000,
        "Square centimeters (cm²)": 0.0001,
        "Square feet (ft²)": 0.09290304,
        "Acres (ac)": 4046.8564224,
    },
}

TEMPERATURE_UNITS = ("Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)")
UNIT_FACTORS["Temperature"] = {unit: 1 for unit in TEMPERATURE_UNITS}


def convert_value(value, category, from_unit, to_unit):
    """Convert a numeric value between two units in the same category."""
    if category not in UNIT_FACTORS:
        raise ValueError("Choose a valid conversion category.")

    units = UNIT_FACTORS[category]
    if from_unit not in units or to_unit not in units:
        raise ValueError("Choose valid units for the selected category.")

    if category == "Temperature":
        return _convert_temperature(value, from_unit, to_unit)

    base_value = value * units[from_unit]
    return base_value / units[to_unit]


def _convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius (°C)":
        celsius = value
    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if to_unit == "Celsius (°C)":
        return celsius
    if to_unit == "Fahrenheit (°F)":
        return celsius * 9 / 5 + 32
    return celsius + 273.15
