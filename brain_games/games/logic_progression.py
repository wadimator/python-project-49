import random

def game_logic(iterator:int) -> list:
    rand_first = random.randint(0, 10)
    cnt_iter = round(random.gauss(9, 1))
    random_index = random.randint(0, cnt_iter)
    result = []
    result.append(rand_first)
    for i in range(cnt_iter):
        if i == random_index:
            result.append("..")
            continue
        rand_first += iterator
        result.append(rand_first)
    return result
