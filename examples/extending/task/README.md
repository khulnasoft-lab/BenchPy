
# Creating a new task (from a new environment)

Here are the steps to create a new task. 

1. Create your `CustomEnvTask` following the example in [`custom_task.py`](custom_task.py).
This is an enum with task entries and some abstract functions you need to implement.

2. Create a `customenv` folder with a yaml configuration file for each of your tasks.
You can see [`customenv`](customenv) for an example.
3. Place your task script in [`benchpy/environments/customenv/common.py`](../../../benchpy/environments) and 
your config in [`benchpy/conf/task`](../../../benchpy/conf/task) (or any other place you want to 
override from).
4. Add `{"customenv/{task_name}": CustomEnvTask.TASK_NAME}` to the 
[`benchpy.environments.task_config_registry`](../../../benchpy/environments/__init__.py) for all tasks.
5. Load it with
```bash
python benchpy/run.py task=customenv/task_name algorithm=...
```

6. (Optional) You can create python dataclasses to use as schemas for your tasks
to validate their config. We are not going to illustrate this here, but if
you want to see an example, check out [`benchpy/environments/vmas`](../../../benchpy/environments/vmas).
