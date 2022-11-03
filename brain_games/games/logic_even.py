

def game_logic(number1: int, number2: int, character: str) -> int:
    if character == "+":
        return number1 + number2
    elif character == "-":
        return number1 - number2
    else:
        return number1 * number2
