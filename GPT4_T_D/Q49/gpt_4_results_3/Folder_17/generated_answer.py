
def if_decimal_is_divisible(num):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < 155:
        fibonacci_list.append(sum(fibonacci_list[-2:]))
    decimal_num = int(num, 2)
    return decimal_num % fibonacci_list[154] == 0
