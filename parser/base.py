import abc


class BaseParser(abc.ABC):

    def __init__(self, path_file: str):
        self.path_file = path_file

    @staticmethod
    def convert_units(quantity: float, unit: str) -> dict:
        convert_data = {}
        conversions = {
            "gallon": ["liter", 3.78],
            "cups": ["ml", 240],
            "pound": ["gr", 454.55],
            "fl. oz.": ["ml", 29.705],
        }
        if unit in conversions:
            quantity, unit = quantity * conversions[unit][1], conversions[unit][0]
        if quantity:
            convert_data["quantity"] = float(f"{quantity:.2f}")
        if unit:
            convert_data["unit"] = unit
        return convert_data

    def read_file(self):
        with open(self.path_file, "r") as f:
            return f.read()

    @abc.abstractmethod
    def parse_data(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def parse_ingredients(self, root):
        raise NotImplementedError

    def parse_file(self) -> dict:
        return self.parse_data()
