import yaml

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml,"rb") as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content