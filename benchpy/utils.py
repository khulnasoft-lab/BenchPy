import importlib
from typing import Any, Dict, Union

import torch
import yaml

DEVICE_TYPING = Union[torch.device, str, int]


def _read_yaml_config(config_file: str) -> Dict[str, Any]:
    with open(config_file) as config:
        yaml_string = config.read()
    config_dict = yaml.safe_load(yaml_string)
    if "defaults" in config_dict.keys():
        del config_dict["defaults"]
    return config_dict


def _class_from_name(name: str):
    name_split = name.split(".")
    module_name = ".".join(name_split[:-1])
    class_name = name_split[-1]
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c
