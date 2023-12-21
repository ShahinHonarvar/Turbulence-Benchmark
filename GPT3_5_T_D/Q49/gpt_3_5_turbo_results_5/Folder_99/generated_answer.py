
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while True:
        next_num = fibonacci[-1] + fibonacci[-2]
        if next_num >= 10**9:
            break
        fibonacci.append(next_num)
    decimal = int(binary, 2)
    return decimal % fibonacci[108] == 0
