__author__ = 'orius123'
from sys import argv
import yaml
import drawer

script, filename = argv

stream = open(filename, 'r')
yaml_src = yaml.load(stream)


def extract_task(task_dict):
    name, value = task_dict.popitem()
    return {'name': name, 'next': value.get('navigate')}


if 'flow' in yaml_src:
    flow_src = yaml_src['flow']
    tasks = flow_src.get('workflow')
    if tasks is None:
        raise LookupError("no workflow tag in a flow - not good")

    tasks_keys = map(extract_task, tasks)

    DEFAULT_FAILURE = 'FAILURE'
    DEFAULT_LAST_STEP = {'SUCCESS': 'SUCCESS', 'FAILURE': DEFAULT_FAILURE}

    for task, next_task in zip(tasks_keys, tasks_keys[1:] + [None]):
        if task.get('next') is None:
            if next_task is None:
                task['next'] = DEFAULT_LAST_STEP
            else:
                task['next'] = {'SUCCESS': next_task['name'], 'FAILURE': DEFAULT_FAILURE}

    drawer.print_ascii(tasks_keys)


else:
    print 'operations are not supported right now'