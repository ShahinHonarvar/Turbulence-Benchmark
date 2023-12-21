
def if_decimal_is_divisible(bin_string):
    fib = [0, 1]
    while len(bin_string) > len(str(fib[-1])):
        fib.append(fib[-1] + fib[-2])
    decimal = int(bin_string, 2)
    return decimal % fib[184] == 0
