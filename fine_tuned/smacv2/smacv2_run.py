import hydra
from benchpy.experiment import Experiment

from benchpy.hydra_config import load_experiment_from_hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path="conf", config_name="config")
def hydra_experiment(cfg: DictConfig) -> None:
    hydra_choices = HydraConfig.get().runtime.choices
    task_name = hydra_choices.task
    algorithm_name = hydra_choices.algorithm

    print(f"\nAlgorithm: {algorithm_name}, Task: {task_name}")
    print("\nLoaded config:\n")
    print(OmegaConf.to_yaml(cfg))

    experiment: Experiment = load_experiment_from_hydra(cfg, task_name=task_name)
    experiment.run()


if __name__ == "__main__":
    hydra_experiment()
