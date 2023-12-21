
def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)

    fibonacci_sequence = [0, 1]
    for i in range(2, 138):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    return number % fibonacci_sequence[137] == 0
