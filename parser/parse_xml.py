import xml.etree.ElementTree as ET

from parser.base import BaseParser


class ParserXML(BaseParser):

    def parse_data(self):
        xml_data = self.read_file()
        root = ET.fromstring(xml_data)
        return {
            "name": root.find("name").text,
            "ingredients": self.parse_ingredients(root),
            "preperations": [root.find("preperations").text],
        }

    def parse_ingredients(self, root):
        ingredients_list = []
        for ingredient in root.findall("ingredients"):
            ingredient_dict = {
                "item": ingredient.find("item").text,
                **self.convert_units(
                    float(ingredient.find("quantity").text),
                    ingredient.find("unit").text,
                ),
            }
            comment = ingredient.find("comment")
            if comment is not None:
                ingredient_dict["comment"] = comment.text
            ingredients_list.append(ingredient_dict)
        return ingredients_list
