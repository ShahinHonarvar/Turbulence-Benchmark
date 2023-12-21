
def if_decimal_is_divisible(binary_str):
    fib_num = [0, 1]
    while len(fib_num) < 179:
        fib_num.append(fib_num[-1] + fib_num[-2])
    decimal_num = int(binary_str, 2)
    if decimal_num % fib_num[178] == 0:
        return True
    else:
        return False
