
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while len(fib) < 195:
        fib.append(fib[-1] + fib[-2])
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return decimal % fib[194] == 0
