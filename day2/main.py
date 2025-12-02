from typing import List, Tuple, Callable

type checker = Callable[[int], bool]


def p1_is_repeated(n: int) -> bool:
    n_str: str = str(n)
    l: int = len(n_str)
    l, r = n_str[:l//2], n_str[l//2:]
    return l == r


def p2_is_repeated(n: int) -> bool:
    n_str: str = str(n)
    l: int = len(n_str)

    buffer: str = ""

    for i in range(l//2):
        buffer += n_str[i]
        if buffer * (l // (i + 1)) == n_str:
            return True

    return False


def solve(input_: List[Tuple[int, int]], part: int):
    result = 0

    check: checker = p1_is_repeated if part == 1 else p2_is_repeated

    for range_ in input_:
        start, end = range_
        for n in range(start, end + 1):
            if check(n):
                result += n

    print(f"part {part}: {result}")


def read_input() -> List[Tuple[int, int]]:
    ranges = []
    line = input()
    for range_ in line.split(','):
        start, end = range_.split('-')
        ranges.append((int(start), int(end)))
    return ranges


input_ = read_input()
solve(input_, 1)
solve(input_, 2)
