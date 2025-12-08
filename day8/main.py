from typing import List
from heapq import nsmallest
from functools import reduce
from operator import mul
from math import sqrt


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.last_connected = (-1, -1)
        self.components = n

    def union(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return

        self.last_connected = (x, y)
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.size[ry] += self.size[rx]
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
            self.size[rx] += self.size[ry]
        self.components -= 1

    def find(self, i: int):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def component_sizes(self):
        for i in range(len(self.parent)):
            self.find(i)
        return {i: self.size[i] for i in range(len(self.parent))
                if self.parent[i] == i}


def distance(a: Box, b: Box) -> float:
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


def solve(input_: List[Box], part: int):
    n = len(input_)
    # P1 test requires 10 connections, input requires 1000
    k = 10 if n == 20 else 1000

    pairs = [(distance(input_[i], input_[j]), i, j)
             for i in range(n) for j in range(i + 1, n)]

    uf = UnionFind(n)

    if part == 1:
        process_pairs = nsmallest(k, pairs, key=lambda x: x[0])
    else:
        process_pairs = sorted(pairs)

    for _, i, j in process_pairs:
        uf.union(i, j)
        if part == 2 and uf.components == 1:
            break

    if part == 1:
        sizes = sorted(uf.component_sizes().values(), reverse=True)[:3]
        print(reduce(mul, sizes))
    else:
        i, j = uf.last_connected
        print(input_[i].x * input_[j].x)


def read_input() -> List[Box]:
    boxes = []
    try:
        while line := input():
            x, y, z = map(int, line.split(","))
            boxes.append(Box(x, y, z))
    except EOFError:
        pass
    return boxes


input_ = read_input()
solve(input_, 1)
solve(input_, 2)
