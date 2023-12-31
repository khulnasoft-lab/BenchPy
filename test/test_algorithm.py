import pytest

from benchpy.algorithms import algorithm_config_registry
from benchpy.algorithms.common import AlgorithmConfig
from benchpy.hydra_config import load_algorithm_config_from_hydra
from hydra import compose, initialize


@pytest.mark.parametrize("algo_name", algorithm_config_registry.keys())
def test_loading_algorithms(algo_name):
    with initialize(version_base=None, config_path="../benchpy/conf"):
        cfg = compose(
            config_name="config",
            overrides=[
                f"algorithm={algo_name}",
                "task=vmas/balance",
            ],
        )
        algo_config: AlgorithmConfig = load_algorithm_config_from_hydra(cfg.algorithm)
        assert algo_config == algorithm_config_registry[algo_name].get_from_yaml()
