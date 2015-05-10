from sys import argv
import yaml
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
nx.shortest_path(G, 'A', 'D', weight='weight')

print '====='
print G.nodes()
print G.edges()
print '===='


nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display

script, filename = argv

txt = open(filename)

stream = open(filename, 'r')
print yaml.load(stream)

print "Here's your file %r:" % filename
print txt.read()