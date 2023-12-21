
def if_perfect_num(my_list):
    if len(my_list) <= 53:
        return False
    num = my_list[53]
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0 and num // i in my_list:
            return True
    return False
