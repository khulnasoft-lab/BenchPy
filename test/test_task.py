import pytest

from benchpy.environments import Task, task_config_registry
from benchpy.hydra_config import load_task_config_from_hydra
from hydra import compose, initialize


@pytest.mark.parametrize("task_name", task_config_registry.keys())
def test_loading_tasks(task_name):
    with initialize(version_base=None, config_path="../benchpy/conf"):
        cfg = compose(
            config_name="config",
            overrides=[
                "algorithm=mappo",
                f"task={task_name}",
            ],
            return_hydra_config=True,
        )
        task_name_hydra = cfg.hydra.runtime.choices.task
        task: Task = load_task_config_from_hydra(cfg.task, task_name=task_name_hydra)
        assert task == task_config_registry[task_name].get_from_yaml()
