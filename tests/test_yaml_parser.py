from parser import ParserYAML


class TestParserYAML:

    def test_read_file(self, mocker, yaml_data):
        parser = ParserYAML("mock_file.yaml")
        mocker.patch.object(parser, "read_file", return_value=yaml_data)
        assert parser.read_file() == yaml_data

    def test_parse_file_ingredients(self, mocker, yaml_data, result_ingredients):
        parser = ParserYAML("mock_file.yaml")
        mocker.patch.object(parser, "read_file", return_value=yaml_data)

        assert parser.parse_data()["ingredients"] == result_ingredients

    def test_parse_file(self, mocker, yaml_data, result_parse_file):
        parser = ParserYAML("mock_file.yaml")
        mocker.patch.object(parser, "read_file", return_value=yaml_data)

        assert parser.parse_data() == result_parse_file
