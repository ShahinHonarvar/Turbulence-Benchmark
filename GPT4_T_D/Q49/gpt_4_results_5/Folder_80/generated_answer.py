
def if_decimal_is_divisible(s):
    binary_num = int(s, 2)
    first_num, second_num = 0, 1
    fib_number = 0

    for i in range(179):
        fib_number = first_num
        first_num, second_num = second_num, first_num + second_num

    return binary_num % fib_number == 0
