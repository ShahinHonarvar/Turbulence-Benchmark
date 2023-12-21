
def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)

    fibo = [0, 1]
    while len(fibo) <= 180:
        fibo.append(fibo[-1] + fibo[-2])

    return num % fibo[180] == 0
