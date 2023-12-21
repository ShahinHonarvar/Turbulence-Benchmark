
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while fibonacci[-1] < int(decimal):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    if len(fibonacci) >= 9:
        return int(decimal) % fibonacci[8] == 0
    else:
        return False
