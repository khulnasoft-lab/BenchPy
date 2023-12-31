__version__ = "1.0.0"

import importlib

import benchpy.algorithms
import benchpy.benchmark
import benchpy.environments
import benchpy.experiment
import benchpy.models

_has_hydra = importlib.util.find_spec("hydra") is not None

if _has_hydra:

    def _load_hydra_schemas():
        from hydra.core.config_store import ConfigStore

        from benchpy.algorithms import algorithm_config_registry
        from benchpy.environments import _task_class_registry
        from benchpy.experiment import ExperimentConfig

        # Create instance to load hydra schemas
        cs = ConfigStore.instance()
        # Load experiment schema
        cs.store(name="experiment_config", group="experiment", node=ExperimentConfig)
        # Load algos schemas
        for algo_name, algo_schema in algorithm_config_registry.items():
            cs.store(name=f"{algo_name}_config", group="algorithm", node=algo_schema)
        # Load task schemas
        for task_schema_name, task_schema in _task_class_registry.items():
            cs.store(name=task_schema_name, group="task", node=task_schema)

    _load_hydra_schemas()
