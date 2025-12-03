from typing import List, Callable

type solver = Callable[[List[int]], int]


def make_largest_joltage(size: int) -> solver:
    def solver(bank: List[int]) -> int:
        deleted = set()
        start = 0
        l: int = len(bank)
        digits = []

        for i in range(size - 1, -1, -1):
            max_val = None
            max_idx = None

            for idx in range(start, l - i):
                if idx not in deleted:
                    if max_val is None or bank[idx] > max_val:
                        max_val = bank[idx]
                        max_idx = idx

            digits.append(max_val)
            deleted.add(max_idx)
            start = max_idx

        return int("".join(map(str, digits)))
    return solver


def solve(input: List[List[int]], part: int):
    solver = make_largest_joltage(2) if part == 1 else make_largest_joltage(12)
    print(f"part {part}: {sum(solver(bank) for bank in input)}")


def read_input() -> List[List[int]]:
    output = []
    try:
        l: str = input()
        while l:
            output.append([int(c) for c in l])
            l: str = input()
    except EOFError:
        pass
    return output


input_ = read_input()
solve(input_, 1)
solve(input_, 2)
