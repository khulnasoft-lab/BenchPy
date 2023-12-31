from benchpy.algorithms import MappoConfig
from benchpy.environments import VmasTask
from benchpy.experiment import Experiment, ExperimentConfig
from benchpy.models.mlp import MlpConfig

if __name__ == "__main__":
    # WARNING: Configuring tasks is only suggested for debugging.
    # For benchmarking, you should use the default configuration/

    # Loads from "benchpy/conf/task/vmas/balance.yaml"
    task = VmasTask.BALANCE.get_from_yaml()

    # You can override from the script
    task.config["n_agents"] = 4  # Change the number of agents to 4

    # Some basic other configs
    algorithm_config = MappoConfig.get_from_yaml()
    experiment_config = ExperimentConfig.get_from_yaml()
    model_config = MlpConfig.get_from_yaml()
    critic_model_config = MlpConfig.get_from_yaml()

    experiment = Experiment(
        task=task,
        algorithm_config=algorithm_config,
        model_config=model_config,
        critic_model_config=critic_model_config,
        seed=0,
        config=experiment_config,
    )
    experiment.run()
