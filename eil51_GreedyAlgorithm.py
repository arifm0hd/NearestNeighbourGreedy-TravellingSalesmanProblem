import numpy as np

# EIL51 data
eil51 = [
    (37, 52), (49, 49), (52, 64), (20, 26), (40, 30),
    (21, 47), (17, 63), (31, 62), (52, 33), (51, 21),
    (42, 41), (31, 32), (5, 25), (12, 42), (36, 16),
    (52, 41), (27, 23), (17, 33), (13, 13), (57, 58),
    (62, 42), (42, 57), (16, 57), (8, 52), (7, 38),
    (27, 68), (30, 48), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (46, 10), (61, 33), (62, 63),
    (63, 69), (32, 22), (45, 35), (59, 15), (5, 6),
    (10, 17), (21, 10), (5, 64), (30, 15), (39, 10),
    (32, 39), (25, 32), (25, 55), (48, 28), (56, 37),
    (30, 40)
]

# calculate the Euclidean distance between two points since the data uses EDGE_WEIGHT_TYPE : EUC_2D,
# which means [city number - coordinate x - coordinate y]
# hence to compare the distance between paths we must first calculate the distance between each cities

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# create a square matrix to store the distances between each city
n = len(eil51)
graph = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        graph[i][j] = euclidean_distance(eil51[i], eil51[j])

# greedy algorithm
best_path = [0]
current_city = 0
for i in range(n-1):
    next_city = -1
    min_distance = float('inf')
    for j in range(n):
        if j not in best_path and graph[current_city][j] < min_distance:
            next_city = j
            min_distance = graph[current_city][j]
    best_path.append(next_city)
    current_city = next_city

def total_path_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i+1]]
    return total_distance

# print the best path
print("Best path:", best_path)
print("Total path distance:", total_path_distance(best_path, graph))