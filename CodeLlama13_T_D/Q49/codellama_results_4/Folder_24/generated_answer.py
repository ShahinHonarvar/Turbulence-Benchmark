
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    decimal = 0
    for i in range(len(binary_list)):
        decimal += binary_list[i] * (2 ** i)
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    return decimal % fibonacci_sequence[55] == 0
