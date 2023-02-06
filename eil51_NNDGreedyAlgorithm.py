import numpy as np
import random

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

# nearest neighbor algorithm from both end points
best_path = [0, 0]
visited = [False for i in range(n)]
visited[0] = True
for i in range(n-2):
    start = best_path[-2]
    end = best_path[-1]
    next_city = -1
    min_distance = float('inf')
    for j in range(n):
        if not visited[j] and graph[start][j] + graph[end][j] - graph[start][end] < min_distance:
            next_city = j
            min_distance = graph[start][j] + graph[end][j] - graph[start][end]
    best_path.append(next_city)
    visited[next_city] = True

# greedy algorithm
greedy_best_path = best_path.copy()
for i in range(2, n):
    index = i

for j in range(i+1, n):
    n = len(eil51)
    if graph[greedy_best_path[index-1]][greedy_best_path[j]] < graph[greedy_best_path[index-1]][greedy_best_path[index]]:
        index = j
    greedy_best_path[i], greedy_best_path[index] = greedy_best_path[index], greedy_best_path[i]

# calculate the total distance of the best path
best_distance = 0
for i in range(1, n):
    best_distance += graph[greedy_best_path[i-1]][greedy_best_path[i]]
best_distance += graph[greedy_best_path[-1]][greedy_best_path[0]]

print("Best Path (Nearest Neighbor Algorithm + Greedy Algorithm):", greedy_best_path)
print("Best Distance:", best_distance)