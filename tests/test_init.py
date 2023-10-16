
import pytest
from data_mapping import map_dicts, map

@pytest.fixture
def input_data():
    return {"name": "John", "age": 30}

@pytest.fixture
def happy_mapping_data():
    return {"name":"person.name", "age":"person.age"}

@pytest.fixture
def depth_mapping_data():
    return {"name":"person.name", "age":{"alpha":"alpha_value"}}

class TestMapDicts:
    def test_happy_path(self, input_data):
        mapping_data = {"name":"person.name", "age":"person.age"}
        expected_output = {
            "person":{
                "name": "John",
                "age": 30
            }
        }
        result = map_dicts(input_data, mapping_data)
    
        assert result == expected_output

    # Data from these test bleed into each other - Why?

    def test_ignore_mapping_depth(self, input_data):
        mapping_data = {"name":"person.name", "age":{"alpha":"alpha_value"}}
        expected_output = {
            "person":{
                "name": "John"
            }
        }
        result = map_dicts(input_data, mapping_data)
    
        assert result == expected_output

class TestMap:

    def test_no_input_no_mapping(self):
        with pytest.raises(Exception):
            result = map()

    def test_no_input(self):
        mapping_data = '{"name": "person.name", "age": "person.age"}'
    
        with pytest.raises(Exception):
            _ = map(mapping = mapping_data)

    def test_no_mapping(self):
        input_data = '{"name": "John", "age": 30}'
    
        with pytest.raises(Exception):
            _ = map(input_data)

    def test_pass_thru_mapping(self):
        input_data = '{"name": "John", "age": 30}'
        mapping_data = '{"name": "name", "age": "age"}'
        expected_output = {"name": "John", "age": 30}

        result = map(input_data, mapping_data)
        assert result == expected_output

    def test_input_mapping_strings(self):
        input_data = '{"name": "John", "age": 30}'
        mapping_data = '{"name":"person.name", "age":"person.age"}'
        expected_output = {
            "person":{
                "name": "John",
                "age": 30
            }
        }
        result = map(input_data, mapping_data)
        assert result == expected_output

