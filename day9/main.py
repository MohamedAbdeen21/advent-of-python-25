from typing import List, Tuple, Dict
from collections import defaultdict

type Segment = Tuple["Tile", "Tile"]
type SegmentSet = Dict[int, List[Tuple[int, int]]]


class Tile:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, tiles: List[Tile]):
        self.tiles = tiles
        self.n = len(tiles)

        self.v_segments: SegmentSet = defaultdict(list)
        self.h_segments: SegmentSet = defaultdict(list)

        for (t1, t2) in zip(tiles, tiles[1:] + [tiles[0]]):
            if t1.x == t2.x:
                y_start, y_end = sorted([t1.y, t2.y])
                self.v_segments[t1.x].append((y_start, y_end))
            elif t1.y == t2.y:
                x_start, x_end = sorted([t1.x, t2.x])
                self.h_segments[t1.y].append((x_start, x_end))

    def rectangle_is_valid(self, t1: Tile, t3: Tile) -> bool:
        x_min, x_max = sorted([t1.x, t3.x])
        y_min, y_max = sorted([t1.y, t3.y])

        for x, segments in self.v_segments.items():
            if not (x_min < x < x_max):
                continue
            for y_start, y_end in segments:
                if y_end > y_min and y_start < y_max:
                    return False

        for y, segments in self.h_segments.items():
            if not (y_min < y < y_max):
                continue
            for x_start, x_end in segments:
                if x_end > x_min and x_start < x_max:
                    return False

        return True


def rectangle_area(a: Tile, b: Tile) -> int:
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def solve(tiles: List[Tile], part: int):
    max_area = 0

    grid = Grid(tiles)

    for i, t1 in enumerate(tiles):
        for t3 in tiles[:i]:
            if part == 1 or grid.rectangle_is_valid(t1, t3):
                max_area = max(max_area, rectangle_area(t1, t3))

    print(f"Part {part}: {max_area}")


def read_input() -> List[Tile]:
    tiles = []
    try:
        while line := input():
            x, y = line.split(",")
            tiles.append(Tile(int(x), int(y)))
    except EOFError:
        pass
    return tiles


input_tiles = read_input()
solve(input_tiles, 1)
solve(input_tiles, 2)
