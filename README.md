# Forest-Burning-and-clusterization
Initializing an agent-based model of forest fire in randomly generated forests with clusters detection.

In this project matrix represents forest where 0-empty space, 1-tree, 2-burning/burned tree. We simulate forest fire by initially
setting the trees on the left edge to be in fire. Fire spreads from burned tree to its direct eight neighbours and make them burn
when they are also trees (not empty spaces). After simulation we detect clusters from burned area. They are labeled and stored
in dictionary so its easy to determine the biggest cluster of burned trees. In this version it is also labeled on the plot and the matrix
is rather small to make it simple to grasp.
