from typing import List, Tuple


class Gift:
    def __init__(self, size: int):
        self.size = size

    @classmethod
    def from_string(cls, s: str):
        size = 0
        parts = s.split()
        for line in parts[1:]:
            size += line.count("#")

        return Gift(size)

    def __repr__(self):
        return f"Gift({self.size})"


class Tree:
    def __init__(self, size: int, gifts: List[int]):
        self.size = size
        self.gifts = gifts

    @classmethod
    def from_string(cls, s: str):
        parts = s.split()
        l, w = parts[0].rstrip(":").split("x")
        size = int(l) * int(w)
        gifts = list(map(lambda g: int(g), parts[1:]))

        return Tree(size, gifts)

    def __repr__(self):
        return f"Tree({self.size}, {self.gifts})"

    def can_fit(self, gifts: List[Gift]):
        return self.size > sum([gifts[i].size * count for i, count
                                in enumerate(self.gifts)])


def read_input() -> Tuple[List[Gift], List[Tree]]:
    gifts = []
    trees = []

    for _ in range(6):
        buffer = ""
        while line := input():
            buffer += line + '\n'
        gifts.append(Gift.from_string(buffer))

    try:
        while line := input():
            trees.append(Tree.from_string(line))
    except EOFError:
        pass

    return (gifts, trees)


def solve(gifts: List[Gift], trees: List[Tree]):
    print(gifts, trees)
    print(sum([tree.can_fit(gifts) for tree in trees]))


gifts, trees = read_input()
solve(gifts, trees)
