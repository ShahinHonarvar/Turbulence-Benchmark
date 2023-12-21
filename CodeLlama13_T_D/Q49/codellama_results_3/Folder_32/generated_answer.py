
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    decimal = 0
    for i in range(len(binary_list)):
        decimal += binary_list[i] * (2 ** i)
    return decimal % 178 == 0
