from typing import Any, List, Self, Union
from pulp import PULP_CBC_CMD, LpProblem, LpMinimize, LpVariable, lpSum, LpInteger
from itertools import combinations
import re


def unwrap[T](value: Union[T, None], msg="unwrap failed") -> T:
    if value is None:
        raise ValueError(msg)
    return value


class LinearSystem:
    def __init__(self, a: List[List[int]], b: List[int]):
        self.a = a
        self.b = b

    def solve(self) -> int:
        m = len(self.a)
        n = len(self.a[0])

        problem = LpProblem("LinearSystem", LpMinimize)

        x = [LpVariable(f"x_{i}", lowBound=0, cat=LpInteger) for i in range(n)]

        problem += lpSum(x)

        for i in range(m):
            problem += lpSum(self.a[i][j] * x[j] for j in range(n)) == self.b[i]

        status = problem.solve(PULP_CBC_CMD(msg=False))

        if status != 1:
            return -1

        return int(sum(unwrap(v.value()) for v in x))


class Machine:
    def __init__(self, lights: int, buttons: List[Any],
                 buttons_bitmask: List[int], joltage: List[int]):
        self.lights = lights
        self.buttons = buttons
        self.buttons_bitmask = buttons_bitmask
        self.joltage = joltage

    @classmethod
    def from_line(cls, line: str) -> Self:
        lights_str = unwrap(re.search(r'\[([.#]+)\]', line)).group(1)
        button_groups = re.findall(r'\(([^)]*)\)', line)
        joltage_str = unwrap(re.search(r'\{([^}]*)\}', line)).group(1)

        # Parse lights: .##. -> 0110 -> 6
        lights_bin = ''.join('1' if c == '#' else '0' for c in lights_str)
        lights = int(lights_bin, 2)
        n = len(lights_str)

        buttons_bitmask = []
        buttons = []
        for group in button_groups:
            if group.strip() == '':
                buttons_bitmask.append(0)
                continue
            idxs = [int(x) for x in group.split(',') if x.strip()]
            buttons.append(idxs)
            bits = ['0'] * n
            for i in idxs:
                bits[i] = '1'
            buttons_bitmask.append(int(''.join(bits), 2))

        joltage = [int(x) for x in joltage_str.split(',')]

        return cls(lights, buttons, buttons_bitmask, joltage)

    def least_presses(self) -> int:
        n = len(self.buttons_bitmask)

        for r in range(1, n + 1):
            for combo in combinations(self.buttons_bitmask, r):
                xor_value = 0
                for b in combo:
                    xor_value ^= b
                if xor_value == self.lights:
                    return r

        return -1

    def to_linear_system(self) -> LinearSystem:
        n = len(self.buttons)
        m = len(self.joltage)

        a = [[0] * n for _ in range(m)]
        for i, button in enumerate(self.buttons):
            for pos in button:
                a[pos][i] = 1

        return LinearSystem(a, self.joltage)


def parse_input() -> List[Machine]:
    machines = []
    try:
        while line := input():
            machines.append(Machine.from_line(line))
    except EOFError:
        pass

    return machines


def solve(machines: List[Machine], part: int):
    if part == 1:
        print(sum(m.least_presses() for m in machines))
    else:
        print(sum(m.to_linear_system().solve() for m in machines))


machines = parse_input()
solve(machines, 1)
solve(machines, 2)
