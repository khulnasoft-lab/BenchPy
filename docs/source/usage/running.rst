Running
=======

Experiments are launched with a `default configuration <https://github.com/khulnasoft-lab/BenchPy/blob/main/benchpy/conf>`__ that
can be overridden in many ways.
To learn how to customize and override configurations
please refer to the :doc:`/concepts/configuring` section.

To see a list of all available algorithms, tasks, and models,
pleas refer to the :doc:`/concepts/components` section.

Command line
------------

To launch an experiment from the command line you can do

.. code-block:: console

   python benchpy/run.py algorithm=mappo task=vmas/balance

.. bash_example_button::
   https://github.com/khulnasoft-lab/BenchPy/blob/main/examples/running/run_experiment.sh

Thanks to `hydra <https://hydra.cc/docs/intro/>`__, you can run benchmarks as multi-runs like:

.. code-block:: console

   python benchpy/run.py -m algorithm=mappo,qmix,masac task=vmas/balance,vmas/sampling seed=0,1

.. bash_example_button::
   https://github.com/khulnasoft-lab/BenchPy/blob/main/examples/running/run_benchmark.sh


The default implementation for hydra multi-runs is sequential, but `parallel <https://hydra.cc/docs/plugins/joblib_launcher/>`__
and `slurm <https://hydra.cc/docs/plugins/submitit_launcher/>`__ launchers are also available.

Script
------

You can also load and launch your :class:`~benchpy.experiment.Experiment` from within a script

.. code-block:: python

   from benchpy.algorithms import MappoConfig
   from benchpy.environments import VmasTask
   from benchpy.experiment import Experiment, ExperimentConfig
   from benchpy.models.mlp import MlpConfig

   experiment = Experiment(
      task=VmasTask.BALANCE.get_from_yaml(),
      algorithm_config=MappoConfig.get_from_yaml(),
      model_config=MlpConfig.get_from_yaml(),
      critic_model_config=MlpConfig.get_from_yaml(),
      seed=0,
      config=ExperimentConfig.get_from_yaml(),
   )
   experiment.run()

.. python_example_button::
   https://github.com/khulnasoft-lab/BenchPy/blob/main/examples/running/run_experiment.py


You can also run multiple experiments in a :class:`~benchpy.benchmark.Benchmark`.

.. code-block:: python

   from benchpy.algorithms import MappoConfig, MasacConfig, QmixConfig
   from benchpy.benchmark import Benchmark
   from benchpy.environments import VmasTask
   from benchpy.experiment import ExperimentConfig
   from benchpy.models.mlp import MlpConfig

   benchmark = Benchmark(
       algorithm_configs=[
           MappoConfig.get_from_yaml(),
           QmixConfig.get_from_yaml(),
           MasacConfig.get_from_yaml(),
       ],
       tasks=[
           VmasTask.BALANCE.get_from_yaml(),
           VmasTask.SAMPLING.get_from_yaml(),
       ],
       seeds={0, 1},
       experiment_config=ExperimentConfig.get_from_yaml(),
       model_config=MlpConfig.get_from_yaml(),
       critic_model_config=MlpConfig.get_from_yaml(),
   )
   benchmark.run_sequential()

.. python_example_button::
   https://github.com/khulnasoft-lab/BenchPy/blob/main/examples/running/run_benchmark.py
