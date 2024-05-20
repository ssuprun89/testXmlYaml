from parser import ParserXML


class TestParserXML:

    def test_read_file(self, mocker, xml_data):
        parser = ParserXML("mock_file.xml")
        mocker.patch.object(parser, "read_file", return_value=xml_data)
        assert parser.read_file() == xml_data

    def test_parse_file_ingredients(self, mocker, xml_data, result_ingredients):
        parser = ParserXML("mock_file.xml")
        mocker.patch.object(parser, "read_file", return_value=xml_data)

        assert parser.parse_data()["ingredients"] == result_ingredients

    def test_parse_file(self, mocker, xml_data, result_parse_file):
        parser = ParserXML("mock_file.xml")
        mocker.patch.object(parser, "read_file", return_value=xml_data)

        assert parser.parse_data() == result_parse_file
