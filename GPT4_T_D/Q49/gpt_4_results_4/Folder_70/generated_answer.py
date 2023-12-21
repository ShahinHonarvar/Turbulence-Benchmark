
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_137 = fib_seq(137)
    if decimal_integer % fib_137 == 0:
        return True
    else:
        return False

def fib_seq(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[-1]
