import re
import math


def simple_solver(a: int, b: int, c: int) -> list:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return []
    if discriminant == 0:
        return [-b / (2 * a)]
    return [(-b + math.sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a)]


def prepare_expr(expr: str) -> list:
    expr = expr.replace(' ', '')
    expr = expr.replace('*', '')
    midle = expr.find('=')
    if midle == -1:
        return [expr, '']
    return [expr[:midle], expr[midle + 1:]]


def to_float(expr: str, regex: re) -> float:
    try:
        expr_piece = expr[regex.search(expr).start():regex.search(expr).end():]
    except AttributeError:
        return 0
    if expr_piece.find('^') != -1:
        expr_piece = expr_piece[:len(expr_piece) - 2:]
        print(f'EXPR PIECE: {expr_piece}')

    try:
        if expr_piece[-1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            expr_piece = expr_piece[:len(expr_piece) - 1:]
            print(f'EXPR PIECE: {expr_piece}')
    except IndexError:
        pass
    if expr_piece == '' or expr_piece == '+':
        return 1
    if expr_piece == '-':
        return -1
    if expr_piece[-1] == '-' or expr_piece[-1] == '+':
        expr_piece = expr_piece[:len(expr_piece) - 1]
    return float(expr_piece)


def parse_string(expr: str) -> list[float]:
    a_pattern = '[+-]?[0-9\.]{0,}([a-z]\^2)'
    b_pattern = '[+-]?[0-9\.]{0,}[a-z](?!\^)'
    c_pattern = '(^|\+|-)[0-9\.]+(\+|-|$)'
    first_regex = re.compile(a_pattern)
    second_regex = re.compile(b_pattern)
    third_regex = re.compile(c_pattern)
    a = to_float(expr, first_regex)
    b = to_float(expr, second_regex)
    c = to_float(expr, third_regex)
    print([a, b, c])
    return [float(a), float(b), float(c)]


def solve_expr(expr: str) -> list[float]:
    left_expr, right_expr = prepare_expr(expr)
    answers = []
    left_a, left_b, left_c = parse_string(left_expr)
    right_a, right_b, right_c = parse_string(right_expr)
    a = left_a - right_a
    b = left_b - right_b
    c = left_c - right_c
    # print(left_a, left_b, left_c)
    # print(right_a, right_b, right_c)
    # print(a, b, c)
    if a == 0:
        if b != 0:
            return [-c / b]
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
    while True:
        some_expr = input()
        print(solve_expr(some_expr))
