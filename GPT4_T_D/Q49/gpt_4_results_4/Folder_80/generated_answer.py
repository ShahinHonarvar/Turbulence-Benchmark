
def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_lst = [0, 1]
    for i in range(178):
        fib_lst.append(fib_lst[-1] + fib_lst[-2])
    return decimal % fib_lst[-1] == 0
