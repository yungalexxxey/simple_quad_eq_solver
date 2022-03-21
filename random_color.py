from fastapi.exceptions import HTTPException

import random


def guess_color(num: int) -> str:
    if num <= 0 or num > 100:
        raise HTTPException(status_code=404, detail='Wrong number')
    random.seed(num)
    rand_number = int((random.random() * 100))
    print(rand_number)
    if rand_number <= 15:
        return "red"
    if rand_number <= 38:
        return "green"
    return 'blue'


guess_color(5)
