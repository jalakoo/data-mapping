# Data Mapping Package
This simple package is used to map data from one dictionary object to another based on a configuration.

## Installation
Cloning and referencing from another project. If using Poetry:
`poetry add --editable /path/to/this_cloned_repo`

Or if using pip:
`pip install --target=d:\somewhere\other\than\the\default data-mapping`

## Usage
The core function: `map(input: str | dict, mapping: str | dict) -> dict` has 2 required arguments:

`input` can be any valid .JSON string or dictionary. An example input dictionary:
```
{
    "name": "John"
}
```

`mapping` should be a single depth dictionary of type [str: str] with the strings being dot notated key-value paths, like:
```
{
    "name": "person.name"
}
```
A dictionary is used to prevent duplicate keys as .JSON notation specifies an object (dictionary) type but not a set.

The *output* dictionary will use the values from the `input` dictionary added to the target key-value paths specified in the `mapping` dictionary. So from the above example, the output dictionary will be:
```
{
    "person": {
        "name": "John"
    }
}
```
