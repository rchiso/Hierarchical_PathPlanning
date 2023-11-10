from cluster.cluster import make_clusters
from input.grid import grid
from graph.make_graph import make_graph
from random_state_generator.random_state_generator import random_state_generator

length = 60
height = 30
num = 4
k = 2 #how much we want to shorten the grid into; for example for k=2 100x100 turns into 50x50; for k=5 100x100 turns into 20x20
rectangle,source,dest = random_state_generator(length,height,num,gap=k+3)

grid = grid(rectangle)

#This will print grid
# grid.print_grid()

clusters = make_clusters(rectangle)
graph = make_graph(clusters,source,dest)
print(graph)

grid.add_graph(graph)
grid.print_grid()
grid.plot_grid()


grid.make_meta_grid(k=k)
meta_clusters = make_clusters(grid.meta_rect)
meta_graph = make_graph(meta_clusters,(grid.meta_rect.shape[0]-1,0),(0,grid.meta_rect.shape[1]-1))
print(meta_graph)
grid.add_graph(meta_graph,type="meta")
grid.print_grid(type="meta")
grid.plot_grid(type="meta")

grid.print_meta_path(meta_graph,k)


