
def if_perfect_num(my_list):
    if len(my_list) <= 24:
        return False
    num = my_list[24]
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and i * (num // i) == num:
            return True
    return False
