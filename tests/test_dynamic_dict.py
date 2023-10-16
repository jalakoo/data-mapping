import pytest
from data_mapping.dynamic_dict import DynamicDict

class TestDynamicDict:
    def test_dynamic_dict_initializes_empty(self):
        dd = DynamicDict()
        assert dd.data == {}

    def test_dynamic_dict_initializes_with_data(self):
        data = {"a": 1, "b": 2}
        dd = DynamicDict(data)
        assert dd.data == data

    def test_dynamic_dict_getval_simple(self):
        data = {"a": {"b": 2}}
        dd = DynamicDict(data)
        assert dd.getval(["a", "b"]) == 2

    def test_dynamic_dict_getval_missing_key(self):
        dd = DynamicDict()
        with pytest.raises(KeyError):
            dd.getval(["a", "b"])

    def test_dynamic_dict_setval_new_key(self):
        dd = DynamicDict()
        dd.setval(["a", "b"], 2)
        assert dd.data == {"a": {"b": 2}}

    def test_dynamic_dict_setval_existing_key(self):
        dd = DynamicDict({"a": {"b": 1}})
        dd.setval(["a", "b"], 2)
        assert dd.data == {"a": {"b": 2}}

    def test_dynamic_dict_to_dict(self):
        data = {"a": 1, "b": 2}
        dd = DynamicDict(data)
        assert dd.to_dict() == data