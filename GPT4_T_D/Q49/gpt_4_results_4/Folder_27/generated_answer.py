
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 87:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fibonacci_87 = fib_seq[-1]
    if decimal % fibonacci_87 == 0:
        return True
    else:
        return False
