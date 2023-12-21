
def if_decimal_is_divisible(binary_str):
    fib_list = [0, 1]
    for i in range(2, 119):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    decimal = int(binary_str, 2)
    return decimal % fib_list[119] == 0
