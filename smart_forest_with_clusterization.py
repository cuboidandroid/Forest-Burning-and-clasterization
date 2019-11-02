# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:22:49 2019

@author: Stanisław
"""

import matplotlib.pyplot as plt
import numpy as np

# CLUSTERING
def clusterize(matrix):

    ToVisit = []           
    clusters = {}
    size = matrix.shape[0]-1
    current_label = 0
    for x in range(1,size+1):
        for y in range(1,size+1):
            if forest[x,y] == 2 and (x,y) not in clusters:
                clusters[(x,y)] = current_label
                ToVisit.append((x,y))
                while not ToVisit == []:
                    c = ToVisit.pop()
                    surr=[(c[0]+1,c[1]), (c[0],c[1]+1), (c[0],c[1]-1), (c[0]-1,c[1])]#,
                          #(c[0]+1,c[1]+1), (c[0]-1,c[1]-1), (c[0]-1,c[1]+1), (c[0]+1,c[1]-1)]
                    for cor in surr:
                        if forest[cor] == 2 and cor not in clusters:
                            clusters[cor] = current_label
                            ToVisit.append(cor)
                current_label +=1
        
    return clusters
 
def burnforest(size, p): #create forest and burn it, return matrix 
    
    # with padding its 8x8 so 0-7
    forest = np.random.choice([0, 1], size=(size,size), p=[1-p, p])
    
    #STARTING FIREWALL (Left side of matrix 0-empty, 1-tree, 2-burning/burned tree)
    forest[:,0] *= 2
    
    # ADJUSTING EDGES
    forest = np.pad(forest, ((1,1),(1,1)), 'constant')
    
    
    # START THE STACK
    ToVisit = []
    
    for x in range (1, size+1):
        for y in range (1, size+1):
            if forest[x,y] == 2:
                ToVisit.append((x,y))
            
    # STACK COMPLETING
    
    while not ToVisit == []:
        c = ToVisit.pop()
        surr=[(c[0]+1,c[1]), (c[0],c[1]+1), (c[0]+1,c[1]+1), (c[0]-1,c[1]),
              (c[0],c[1]-1), (c[0]-1,c[1]-1), (c[0]-1,c[1]+1), (c[0]+1,c[1]-1)]
        for cor in surr:
            if forest[cor] == 1:
                forest[cor] = 2
                ToVisit.append(cor)
                
    return forest
 
matrix_size = 30                
forest = burnforest(matrix_size, 0.49)
clusters =  clusterize(forest)

fig, ax = plt.subplots()
im = ax.imshow(forest)   

for x in range(1,matrix_size+1):
    for y in range(1,matrix_size+1):
        if (x,y) in clusters:
            text = ax.text(y, x, clusters[(x,y)],
                           ha="center", va="center", color="k")
plt.show()
        