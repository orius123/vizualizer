from sys import argv
import yaml

script, filename = argv

txt = open(filename)

stream = open(filename, 'r')
yaml_src = yaml.load(stream)

print '======================'
print '======================'
print '======================'

if 'flow' in yaml_src:
    print 'flow'
    tasks = yaml_src['flow'].get('workflow')
    if tasks is None:
        raise ValueError("no workflow tag in a flow - not good")

    print tasks

    tasks_keys = map(lambda x: {'name': x.keys()[0], 'next': x.get('navigate')}, tasks)
    print tasks_keys

else:
    print 'operations are not supported right now'

print '======================'
print '======================'
print '======================'

#
# print "Here's your file %r:" % filename
# print txt.read()