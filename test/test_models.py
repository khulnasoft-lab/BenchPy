import pytest

from benchpy.hydra_config import load_model_config_from_hydra
from benchpy.models import model_config_registry

from benchpy.models.common import SequenceModelConfig
from hydra import compose, initialize


@pytest.mark.parametrize("model_name", model_config_registry.keys())
def test_loading_simple_models(model_name):
    with initialize(version_base=None, config_path="../benchpy/conf"):
        cfg = compose(
            config_name="config",
            overrides=[
                "algorithm=mappo",
                "task=vmas/balance",
                f"model=layers/{model_name}",
            ],
        )
        model_config = load_model_config_from_hydra(cfg.model)
        assert model_config == model_config_registry[model_name].get_from_yaml()


@pytest.mark.parametrize("model_name", model_config_registry.keys())
def test_loading_sequence_models(model_name, intermidiate_size=10):
    with initialize(version_base=None, config_path="../benchpy/conf"):
        cfg = compose(
            config_name="config",
            overrides=[
                "algorithm=mappo",
                "task=vmas/balance",
                "model=sequence",
                f"model/layers@model.layers.l1={model_name}",
                f"model/layers@model.layers.l2={model_name}",
                f"+model/layers@model.layers.l3={model_name}",
                f"model.intermediate_sizes={[intermidiate_size,intermidiate_size]}",
            ],
        )
        hydra_model_config = load_model_config_from_hydra(cfg.model)
        layer_config = model_config_registry[model_name].get_from_yaml()
        yaml_config = SequenceModelConfig(
            model_configs=[layer_config, layer_config, layer_config],
            intermediate_sizes=[intermidiate_size, intermidiate_size],
        )
        assert hydra_model_config == yaml_config
