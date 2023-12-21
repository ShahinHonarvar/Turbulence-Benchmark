
def if_decimal_is_divisible(binary_string):
    fib_num_list = [0, 1]
    while len(fib_num_list) < 185:
        fib_num_list.append(fib_num_list[-1] + fib_num_list[-2])
    decimal = int(binary_string, 2)
    return decimal % fib_num_list[184] == 0
