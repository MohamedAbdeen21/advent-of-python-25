from typing import Tuple, List, Self


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __contains__(self, item):
        return self.start <= item <= self.end

    def __repr__(self):
        return f"{self.start}-{self.end}"

    def __lt__(self, other):
        return self.start < other.start

    def count(self):
        return self.end - self.start + 1

    def merge(self, other: Self) -> bool:
        if self.end < other.start:
            return False

        if other.start <= self.end <= other.end:
            self.end = other.end

        return True


def merge_sorted_intervals(intervals: List[Interval]) -> int:
    finalized_intervals = []

    i1, i2 = 0, 1

    while i2 < len(intervals):
        if not intervals[i1].merge(intervals[i2]):
            finalized_intervals.append(intervals[i1])
            i1 = i2

        i2 += 1

    finalized_intervals.append(intervals[i1])

    return sum([i.count() for i in finalized_intervals])


def solve(intervals: List[Interval], ingredients: List[int], part: int):
    count = 0
    if part == 1:
        for i in ingredients:
            for interval in intervals:
                if i in interval:
                    count += 1
                    break
    elif part == 2:
        intervals.sort()
        count = merge_sorted_intervals(intervals)

    print(f"part {part}: {count}")


def read_input() -> Tuple[List[Interval], List[int]]:
    intervals = []
    ingredients = []

    try:
        while True:
            line = input()
            if line == "":
                break
            start = int(line.split("-")[0])
            end = int(line.split("-")[1])
            intervals.append(Interval(start, end))
    except EOFError:
        pass

    try:
        while True:
            line = input()
            if line == "":
                break
            ingredients.append(int(line))
    except EOFError:
        pass

    return intervals, ingredients


(intervals, ingredients) = read_input()
solve(intervals, ingredients, 1)
solve(intervals, ingredients, 2)
