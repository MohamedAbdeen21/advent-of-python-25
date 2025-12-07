from typing import List

type Grid = List[List[str]]


def read_input() -> Grid:
    output = []
    try:
        while line := input():
            output.append(list(line))
    except EOFError:
        pass
    return output


def solve(grid):
    n, m = len(grid), len(grid[0])

    table = [[0] * m for _ in range(n)]

    sj = grid[0].index("S")
    table[0][sj] = 1

    splits = 0

    for i in range(n - 1):
        for j in range(m):
            w = table[i][j]
            if w == 0:
                continue

            cell_below = grid[i + 1][j]

            if cell_below == ".":
                table[i + 1][j] += w

            elif cell_below == "^":
                splits += 1

                table[i + 1][j - 1] += w
                table[i + 1][j + 1] += w

    print("part 1:", splits)
    print("part 2:", sum(table[n - 1]))


input_ = read_input()
# I usually do part 1 and part 2, but since both solutions are
# almost identical, we'll do them both in one pass
solve(input_)
