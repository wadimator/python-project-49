import random


def game_logic() -> list:
    iterator = random.randint(1, 10)
    rand_first = random.randint(0, 10)
    cnt_iter = round(random.gauss(9, 1))
    random_index = random.randint(0, cnt_iter - 1)
    result_list = [rand_first]
    result_number = 0
    for i in range(cnt_iter):
        if i == random_index:
            result_number = result_list[-1] + iterator
            result_list.append("..")
            rand_first += iterator
        rand_first += iterator
        result_list.append(rand_first)
    return [result_list, result_number]
