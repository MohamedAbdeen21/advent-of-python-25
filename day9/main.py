from typing import List


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def rectangle_area(t1: Tile, t2: Tile):
    return abs(t1.x - t2.x + 1) * abs(t1.y - t2.y + 1)


def solve(input_: List[Tile], part: int):
    areas = [rectangle_area(t1, t2) for t1 in input_ for t2 in input_]
    print(f"Part {part}: {max(areas)}")


def read_input() -> List[Tile]:
    tiles = []
    try:
        while line := input():
            x, y = line.split(",")
            tiles.append(Tile(int(x), int(y)))
    except EOFError:
        pass
    return tiles


input_ = read_input()
solve(input_, 1)
# solve(input_, 2)
