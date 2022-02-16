import re
import math


def prepare_expr(expr: str) -> list:
    _right_side_pattern_ = '(=)-?[\d\.]+'
    regex = re.compile(_right_side_pattern_)
    try:
        result = expr[regex.search(expr).start() + 1:regex.search(expr).end():]
    except AttributeError:
        return [expr, 0]
    return [expr[:expr.find('='):], float(result)]


def to_float(expr: str, regex: re) -> float:
    try:
        expr_piece = expr[regex.search(expr).start():regex.search(expr).end():]
    except AttributeError:
        return 0
    if expr_piece.find('^') != -1:
        expr_piece = expr_piece[:len(expr_piece) - 3:]
    if expr_piece.find('x') != -1:
        expr_piece = expr_piece[:len(expr_piece) - 1:]
    if expr_piece == '' or expr_piece == '+':
        return 1
    if expr_piece == '-':
        return -1
    if expr_piece[-1] == '-' or expr_piece[-1] == '+':
        expr_piece = expr_piece[:len(expr_piece) - 1]
    return float(expr_piece)


def parse_string(expr: str) -> list[float]:
    a_pattern = '[+-]?[0-9\.]{0,}(x\^2)'
    b_pattern = '[+-]?[\d\.]{0,}x(?!\^)'
    c_pattern = '(^|\+|-)[0-9\.]+(\+|-|$)'
    first_regex = re.compile(a_pattern)
    second_regex = re.compile(b_pattern)
    third_regex = re.compile(c_pattern)
    a = to_float(expr, first_regex)
    b = to_float(expr, second_regex)
    c = to_float(expr, third_regex)
    return [float(a), float(b), float(c)]


def solve_expr(expr: str) -> list[float]:
    expr, _rightside_ = prepare_expr(expr)
    answers = []
    a, b, c = parse_string(expr)
    c = c - _rightside_
    if a == 0:
        if b != 0:
            return [-c/b]
        else:
            return []
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return answers
    elif disc > 0:
        answers.append((-b + math.sqrt(disc)) / (2 * a))
        answers.append((-b - math.sqrt(disc)) / (2 * a))
        return answers
    else:
        answers.append(-b / (2 * a))
    return answers


if __name__ == '__main__':
    some_expr = input()
    print(solve_expr(some_expr))
