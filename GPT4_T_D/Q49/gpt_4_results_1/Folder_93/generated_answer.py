
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)

    fib_num = [0, 1]
    for i in range(2, 60):
        fib_num.append(fib_num[i - 1] + fib_num[i - 2])

    return decimal % fib_num[59] == 0
