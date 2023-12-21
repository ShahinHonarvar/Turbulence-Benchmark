
def if_decimal_is_divisible(binary):
    num = int(binary, 2)
    fibonacci_seq = [0, 1] + [fibonacci_seq[i - 1] + fibonacci_seq[i - 2] for i in range(2, 190)]
    return (num % fibonacci_seq[190]) == 0
