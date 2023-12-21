
def if_decimal_is_divisible(binary_num):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < 190:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    decimal_num = int(binary_num, 2)
    return decimal_num % fibonacci_sequence[190] == 0
