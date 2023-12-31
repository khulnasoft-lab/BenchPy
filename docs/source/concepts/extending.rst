Extending
=========


One of the core tenets of BenchPy is allowing users to leverage the existing algorithm
and tasks implementations to benchmark their newly proposed solution.

For this reason we expose standard interfaces with simple abstract methods
for :class:`~benchpy.algorithms.Algorithm`, :class:`~benchpy.environments.Task` and :class:`~benchpy.models.Model`.\

To introduce your solution in the library, you just need to implement the abstract methods
exposed by these base classes which use objects from the  :torchrl:`null` `TorchRL <https://github.com/pytorch/rl>`__ library.

Here is an example on how you can create a custom algorithm

.. python_example_button::
   https://github.com/khulnasoft-lab/BenchPy/blob/main/examples/extending/algorithm

Here is an example on how you can create a custom task

.. python_example_button::
   https://github.com/khulnasoft-lab/BenchPy/blob/main/examples/extending/task

Here is an example on how you can create a custom model

.. python_example_button::
   https://github.com/khulnasoft-lab/BenchPy/blob/main/examples/extending/model
