
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    first_num = 0
    second_num = 1
    for i in range(86):
        temp = first_num
        first_num = second_num
        second_num = temp + second_num
    return decimal_integer % second_num == 0
