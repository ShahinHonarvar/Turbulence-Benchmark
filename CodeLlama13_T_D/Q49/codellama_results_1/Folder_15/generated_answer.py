
def if_decimal_is_divisible(binary_repr):
    fibonacci_sequence = [0, 1]
    while True:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_fib in fibonacci_sequence:
            break
        fibonacci_sequence.append(next_fib)
    if int(binary_repr, 2) % fibonacci_sequence[9]:
        return True
    else:
        return False
