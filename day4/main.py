from typing import List, Iterator, Tuple


class Grid[T]:
    def __init__(self, data: List[List[T]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __getitem__(self, i: int) -> List[T]:
        return self.data[i]

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        for i in range(self.rows):
            for j in range(self.cols):
                yield i, j

    def neighbors(self, x: int, y: int) -> Iterator[Tuple[int, int]]:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    yield i, j


def count_neighbours(grid: Grid[str], x: int, y: int) -> int:
    return sum(1 for i, j in grid.neighbors(x, y) if grid[i][j] == "@")


def remove_neighbour(grid: Grid[int], x: int, y: int) -> None:
    for i, j in grid.neighbors(x, y):
        grid[i][j] -= 1


def solve(input_: Grid[str], part: int) -> None:
    rows, cols = input_.rows, input_.cols
    neighbours = Grid([[0] * cols for _ in range(rows)])

    for i, j in input_:
        if input_[i][j] == '@':
            neighbours[i][j] = count_neighbours(input_, i, j)

    count = 0

    while True:
        changed = False

        for i, j in neighbours:
            if input_[i][j] == '@' and neighbours[i][j] < 4:
                count += 1
                if part == 2:
                    input_[i][j] = '.'
                    remove_neighbour(neighbours, i, j)
                    changed = True

        if not changed:
            break

    print(f"part {part}: {count}")


def read_input() -> Grid[str]:
    rows = []
    try:
        while True:
            rows.append([ch for ch in input()])
    except EOFError:
        pass
    return Grid(rows)


input_ = read_input()
solve(input_, 1)
solve(input_, 2)
