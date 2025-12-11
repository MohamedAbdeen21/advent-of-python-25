from typing import List, Dict, Set, Tuple, Optional

type Matrix = Dict[str, List[str]]
type Memo = Dict[Tuple[str, bool, bool], int]


class Parameters:
    def __init__(self, start: str, must_have: Optional[List[str]] = None):
        self.start = start
        self.must_have = must_have if must_have else [None, None]


class Graph:
    def __init__(self, matrix: Matrix, param: Parameters):
        self.adj = matrix
        self.start = param.start
        self.end = "out"
        self.req1 = param.must_have[0]
        self.req2 = param.must_have[1]
        self.path: Set[str] = set()
        self.memo: Memo = {}

    def dfs(self) -> int:
        return self._dfs(self.start, False, False)

    def _dfs(self, node: str, have1: bool, have2: bool) -> int:
        if self.req1 is not None:
            have1 = have1 or (node == self.req1)
        if self.req2 is not None:
            have2 = have2 or (node == self.req2)

        if node == self.end:
            if (self.req1 is None) or (have1 and have2):
                return 1
            return 0

        if node in self.path:
            return 0

        key = (node, have1, have2)
        if key in self.memo:
            return self.memo[key]

        self.path.add(node)
        total = 0
        for neigh in self.adj.get(node, []):
            total += self._dfs(neigh, have1, have2)
        self.path.remove(node)

        self.memo[key] = total
        return total


def read_input() -> Matrix:
    matrix: Matrix = {}
    try:
        while line := input():
            parts = line.split()
            matrix[parts[0].rstrip(":")] = parts[1:]
    except EOFError:
        pass
    return matrix


def solve(matrix: Matrix, part: int):
    param = Parameters("you") if part == 1 \
            else Parameters("svr", ["dac", "fft"])

    graph = Graph(matrix, param)
    total_paths = graph.dfs()

    print(total_paths)


matrix = read_input()
solve(matrix, 1)
solve(matrix, 2)
