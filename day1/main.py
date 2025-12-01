from typing import Callable, List, Optional


type callback = Callable[[int, int], int]


def process_step(current: int, step: str, callback: callback):
    dir, distance = step[0], step[1:]
    distance: int = int(distance)
    if dir == "L":
        distance = -distance
    callback(current, distance)
    return (current + distance) % 100


def p1_callback(counter: List[int]) -> callback:
    def cb(current: int, distance: int) -> int:
        if (current + distance) % 100 == 0:
            counter[0] += 1
    return cb


def p2_callback(counter: List[int]) -> callback:
    def cb(current: int, distance: int) -> int:
        start = current
        end = current + distance

        if distance < 0:
            start, end = -start, -end

        counter[0] += end // 100 - start // 100
    return cb


def read_input() -> list[str]:
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return lines


def solve(steps: List[str], part: int):
    # ints are passed by value, lists by ref
    counter: List[int] = [0]

    call: Optional[callback] = None
    if part == 1:
        call = p1_callback
    elif part == 2:
        call = p2_callback

    current: int = 50
    for step in steps:
        current = process_step(current, step, call(counter))

    print(f"part {part}: {counter[0]}")


input_ = read_input()
solve(input_, 1)
solve(input_, 2)
