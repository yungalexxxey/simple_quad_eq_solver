from fastapi import FastAPI

from math_expr_parser import solve_expr
from math_expr_parser import simple_solver
from random_color import guess_color

app = FastAPI()


@app.get("/hardsolve")
async def hard_solve(expr: str):
    return {"data": solve_expr(expr)}


@app.get("/solve/")
async def simple_solve(a: int = 0, b: int = 0, c: int = 0):
    return {"data": simple_solver(a, b, c)}


@app.get("/guess")
async def guess(num: int = 0):
    return {"data": guess_color(num)}
