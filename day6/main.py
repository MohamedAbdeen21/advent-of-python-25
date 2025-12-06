import enum
from typing import List, Callable
from functools import reduce

type ProblemInput = List[str]


class Operator(enum.Enum):
    NONE = ""
    ADD = "+"
    MULTIPLY = "*"

    def __call__(self) -> Callable[[int, int], int]:
        if self == Operator.ADD:
            return lambda x, y: x + y
        elif self == Operator.MULTIPLY:
            return lambda x, y: x * y
        else:
            raise Exception(f"Invalid operator {self}")


class Problem:
    def __init__(self):
        self.inputs = []
        self.operator = Operator.NONE

    def __repr__(self):
        return f"Problem({self.inputs}, {self.operator})"

    def add_number(self, number: int):
        self.inputs.append(number)

    def set_operator(self, operator: Operator):
        self.operator = operator

    def get_result(self) -> int:
        return reduce(self.operator(), self.inputs)


def transpose(matrix: List[List[str]]) -> List[List[str]]:
    return list(map(list, zip(*matrix)))


def p2(input_: ProblemInput) -> List[Problem]:
    transposed = transpose([[char for char in line] for line in input_])

    problems = []
    problem = Problem()

    for line in transposed:
        if all(" " in s for s in line):
            problems.append(problem)
            problem = Problem()
            continue

        if line[-1] in "+*":
            problem.set_operator(Operator(line[-1]))
            line = line[:-1]

        num_str = "".join(filter(lambda x: x.isnumeric() and x != "", line))
        problem.add_number(int(num_str))

    problems.append(problem)

    return problems


def p1(input_: ProblemInput) -> List[Problem]:
    problems = []

    for number in input_[0].split():
        problems.append(Problem())
        problems[-1].add_number(int(number))

    for line in input_[1:]:
        elements = line.split()
        if elements[0].isdigit():
            for p, value in zip(problems, elements):
                p.add_number(int(value))
        else:
            for p, op in zip(problems, elements):
                p.set_operator(Operator(op))

    return problems


def solve(input_: ProblemInput, part: int):
    if part == 1:
        problems = p1(input_)
    elif part == 2:
        problems = p2(input_)
    else:
        raise Exception(f"Invalid part {part}")

    print(f"part {part}: ", sum(problem.get_result() for problem in problems))


def read_input() -> ProblemInput:
    all_input = []
    try:
        while line := input():
            all_input.append(line)
    except EOFError:
        pass
    return all_input


input_ = read_input()
solve(input_, 1)
solve(input_, 2)
