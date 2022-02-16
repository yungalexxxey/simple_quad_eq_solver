from fastapi import FastAPI
from math_expr_parser import solve_expr

app = FastAPI()


@app.get("/")
async def solve(expr: str):
    return {"data": solve_expr(expr)}
