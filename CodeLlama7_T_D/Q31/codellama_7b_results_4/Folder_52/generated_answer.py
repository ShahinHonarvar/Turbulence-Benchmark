
def if_perfect_num(lst):
    if len(lst) < 478:
        return False

    perfect_num = lst[478]
    factor_sum = 0

    for i in range(1, perfect_num // 2 + 1):
        if perfect_num % i == 0:
            factor_sum += i

    return factor_sum == perfect_num
