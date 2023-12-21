
def all_ints_div_by_num(lst):
    divisible_by_14 = []
    for i in range(43, 77):
        if lst[i] % 14 == 0:
            divisible_by_14.append(lst[i])
    return divisible_by_14
