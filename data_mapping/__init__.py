import json
from data_mapping.dynamic_dict import DynamicDict

def map_dicts(input: dict, mapping: dict) -> dict:
    """
    Map input dictionary to an output dictionary with a mapping dictionary.

    Args:
        input: Any dict
        mapping: Any dict where the keys are a string representation of the input key paths and the values are a string representation of the target key paths. Only the top level key-value pairs are needed. Nested data will be ignored.

    Returns:
        A dictionary of mapped data. It will be a dict similar to the model, but where the values will be replaced with the input values defined by the mapping dictionary.

    Raises:
        ValueError if the args are not dictionaries.
    """
    if isinstance(input, dict) is False:
        raise ValueError(f'Input arg should be a dictionary')

    if isinstance(mapping, dict) is False:
        raise ValueError(f'Mapping arg should be a dictionary')

    # Prep dynamic dictionaries
    input_dd = DynamicDict(input)
    mapping_dd = DynamicDict()

    # Read through mapping file and generate a new dictionary structurally similar to the model
    for input_paths_str, model_paths_str in mapping.items():
        # Skip any other than str paths
        if isinstance(model_paths_str, str) == False:
            print(f'non-str model path: {model_paths_str}')
            continue
        print(f'processing model path: {model_paths_str}')
        input_path = input_paths_str.split(".")
        model_path = model_paths_str.split(".")
        input_value = input_dd.getval(input_path)
        mapping_dd.setval(model_path, input_value)

    return mapping_dd.to_dict()

def map(input: str|dict, mapping: str|dict = None) -> dict:
    """
    Map input .json data to a model .json with an optional mapping .json file.

    Args:
        input: Any stringified .json object or a dict
        mapping: Any stringified .json object or a dict where the keys are a string representation of the input key paths and the values are a string representation of the model key paths. Only the top level key-value pairs are needed. Nested data will be ignored

    Returns:
        A dictionary of mapped data. It will be a dict similar to the model, but where the values will be replaced with the input values defined by the mapping dictionary.

    Raises:
        json.JSONDecodeError if input args are strings and not parsable to dictionaries. ValueError if the args can not be converted to dictionaries.
    """

    # Convert any argument string to dicts
    if isinstance(input, str) is True:
        input = json.loads(input)
    
    if isinstance(mapping, str) is True:
        mapping = json.loads(mapping)

    return map_dicts(input, mapping)