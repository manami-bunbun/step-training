#!/usr/bin/env python3

import itertools
import random
import sys
import math

import numpy as np
from common import print_tour, read_input

# Challenge 0　3518.10
# Challenge 1　3942.55
# Challenge 2　5303.98
# Challenge 3　10459.71
# Challenge 4　12169.94
# Challenge 5　24016.19
# Challenge 6　46470.69


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def issame(self, x, y):
        return self.find(x) == self.find(y)


def solve(cities):
    N = len(cities)
    return kruskal(cities, N)


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# https://qiita.com/flowerrr__lily/items/6679f9496d0079fa0dd2#%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%AB%E3%83%AB%E6%B3%95
def kruskal(cities, N):
    
    # Union-Findデータ構造の初期化
    uf = UnionFind(N)
    
    # 各都市間の距離を計算して保存
    distances = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            distances[i][j] = distance(cities[i], cities[j])
            distances[j][i] = distances[i][j]

    # エッジを距離の昇順でソート
    sorted_edges = []
    for i in range(N):
        for j in range(i + 1, N):
            sorted_edges.append((i, j, distances[i][j]))
    sorted_edges.sort(key=lambda x: x[2])

    # ツアー構築のための関数
    def go_next():
        for i in range(len(neighbors[next_city])):
            if neighbors[next_city][i] in unvisited_cities:
                return neighbors[next_city][i]
        return None

    # 隣接リストの初期化
    neighbors = [[] for _ in range(N)]
    
    # Kruskalのアルゴリズムによりツアー構築
    for k in range(N * (N - 1) // 2):
        i, j, dist = sorted_edges[k]
        if not uf.issame(i, j) and len(neighbors[i]) < 2 and len(neighbors[j]) < 2:
            neighbors[i].append(j)
            neighbors[j].append(i)
            uf.unite(i, j)

    # 2つの孤立した都市をつなぐエッジを追加
    isolated_cities = []
    for i in range(N):
        if len(neighbors[i]) == 1:
            isolated_cities.append(i)
    neighbors[isolated_cities[0]].append(isolated_cities[1])
    neighbors[isolated_cities[1]].append(isolated_cities[0])

    # ツアーの構築
    start_city = 0
    unvisited_cities = set(range(1, N))
    tour = [start_city]
    next_city = neighbors[start_city][0]
    while unvisited_cities:
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        next_city = go_next()

    return tour
    

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
