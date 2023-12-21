
def if_decimal_is_divisible(bin_string):
    fibonacci_seq = [0, 1]
    for _ in range(47):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])

    decimal = int(bin_string, 2)
    return decimal % fibonacci_seq[-1] == 0
