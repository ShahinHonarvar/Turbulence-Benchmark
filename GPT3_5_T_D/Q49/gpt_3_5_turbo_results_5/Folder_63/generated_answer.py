
def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    fibonacci = 1
    while fibonacci <= int(binary_str, 2):
        fibonacci = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(fibonacci)
    if binary_str[-1] == '0' and fibonacci % 144 == 0:
        return True
    else:
        return False
