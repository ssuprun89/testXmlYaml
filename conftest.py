import pytest


@pytest.fixture
def xml_data():
    return '<?xml version="1.0" encoding="UTF-8" ?> <root>    <name>pudding</name>    <ingredients>       <item>milk</item>       <quantity>1</quantity>       <unit>gallon</unit>    </ingredients>    <ingredients>       <item>sugar</item>       <quantity>2</quantity>       <unit>cups</unit>    </ingredients>    <ingredients>       <item>vanilla</item>       <quantity>10</quantity>       <unit>ml</unit>    </ingredients>    <ingredients>       <item>egg yolks</item>       <quantity>12</quantity>       <comment>room temperature</comment>       <unit></unit>    </ingredients>    <preperations>omitted for brevity</preperations> </root>'


@pytest.fixture
def yaml_data():
    return """---
name: pudding
ingredients:
- item: milk
  quantity: 1
  unit: gallon
- item: sugar
  quantity: 2
  unit: cups
- item: vanilla
  quantity: 10
  unit: ml
- item: egg yolks
  quantity: 12
  comment: room temperature
preperations:
- omitted for brevity
"""


@pytest.fixture
def result_ingredients():
    return [
        {"item": "milk", "quantity": 3.78, "unit": "liter"},
        {"item": "sugar", "quantity": 480.0, "unit": "ml"},
        {"item": "vanilla", "quantity": 10.0, "unit": "ml"},
        {"item": "egg yolks", "quantity": 12.0, "comment": "room temperature"},
    ]


@pytest.fixture
def result_parse_file():
    return {
        "name": "pudding",
        "ingredients": [
            {"item": "milk", "quantity": 3.78, "unit": "liter"},
            {"item": "sugar", "quantity": 480.0, "unit": "ml"},
            {"item": "vanilla", "quantity": 10.0, "unit": "ml"},
            {"item": "egg yolks", "quantity": 12.0, "comment": "room temperature"},
        ],
        "preperations": ["omitted for brevity"],
    }
