
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_num = get_fibonacci_number(187)
    return decimal % fib_num == 0

def get_fibonacci_number(n):
    fib_numbers = [0, 1]
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers[-1]
