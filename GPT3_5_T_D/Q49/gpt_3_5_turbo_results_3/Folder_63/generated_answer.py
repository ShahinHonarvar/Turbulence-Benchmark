
def if_decimal_is_divisible(num):
    fib_sequence = [0, 1]
    while len(str(fib_sequence[-1])) < len(num):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    num = int(num, 2)
    if num % fib_sequence[143] == 0:
        return True
    else:
        return False
