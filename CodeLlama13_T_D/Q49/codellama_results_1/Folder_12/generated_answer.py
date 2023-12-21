
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_seq = [0]
    a, b = 0, 1
    while True:
        fibonacci_seq.append(a)
        a, b = b, a + b
        if len(fibonacci_seq) == 67:
            break
    return decimal % fibonacci_seq[66] == 0
