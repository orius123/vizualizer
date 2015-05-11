import sys
from sys import argv
import yaml
import matplotlib.pyplot as plt
import networkx as nx


script, filename = argv

txt = open(filename)

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


    G = nx.MultiDiGraph(name="flow")
    weight = 1

    for task, next_task in zip(tasks_keys, tasks_keys[1:] + [None]):
        if task.get('next') is None:
            if next_task is None:
                task['next'] = DEFAULT_LAST_STEP
            else:
                task['next'] = {'SUCCESS': next_task['name'], 'FAILURE': DEFAULT_FAILURE}
        for nav in task.get('next').values():
            G.add_edge(task['name'], nav, weight=weight)
            weight += 1

        G.add_node(task['name'])
    print tasks_keys

    nx.draw_spectral(G, with_labels=True, node_size=7000, node_shape='p', node_color="c")
    # plt.savefig("house_with_colors.png")
    plt.title(flow_src['name'])
    plt.show()

else:
    print 'operations are not supported right now'

sys.exit()