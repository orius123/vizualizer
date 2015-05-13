import suml.yuml2dot
import suml.common
import sys


def print_ascii(nodes):
    # import drawer
    # drawer.print_ascii()
    spec = ""
    for node in nodes:
        node_name = node['name']
        for edge, next_node in node['next'].iteritems():
            spec += "[" + node_name + "]" + "-" + edge + " >" + "[" + next_node + "],"

    class Object(object):
        pass

    options = Object()
    options.png = True
    # options.svg = True
    options.scruffy = True
    options.shadow = False
    options.font = suml.common.defaultScruffyFont()

    fout = sys.stdout
    # print spec
    suml.yuml2dot.transform(spec, fout, options)