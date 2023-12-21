
def if_decimal_is_divisible(num):
    fibonacci = [0, 1]
    for i in range(2, 16):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    decimal_num = int(num, 2)
    if decimal_num % fibonacci[15] == 0:
        return True
    else:
        return False
