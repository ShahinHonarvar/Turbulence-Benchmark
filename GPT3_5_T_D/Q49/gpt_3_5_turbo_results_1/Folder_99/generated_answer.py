
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while len(fib) < 110:
        fib.append(fib[-1] + fib[-2])
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    if decimal % fib[109] == 0:
        return True
    else:
        return False
