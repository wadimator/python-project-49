

def game_logic(number1: int) -> str:
    for i in range(2, (number1 // 2) + 1):
        if number1 % i == 0:
            return "no"
    return "yes"
