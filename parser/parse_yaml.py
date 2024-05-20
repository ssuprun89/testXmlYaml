import yaml
from parser.base import BaseParser


class ParserYAML(BaseParser):

    def parse_data(self) -> dict:
        yaml_data = self.read_file()
        data = yaml.safe_load(yaml_data)
        self.parse_ingredients(data)
        return data

    def parse_ingredients(self, root: dict) -> None:
        for ingredient in root["ingredients"]:
            ingredient.update(
                self.convert_units(
                    float(ingredient.get("quantity")), ingredient.get("unit")
                )
            )
