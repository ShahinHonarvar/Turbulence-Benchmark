
def if_perfect_num(my_list):
    if len(my_list) <= 67:
        return False

    perfect_number = my_list[67]
    factor_sum = 0

    for i in range(1, perfect_number // 2 + 1):
        if perfect_number % i == 0:
            factor_sum += i

    return factor_sum == perfect_number
