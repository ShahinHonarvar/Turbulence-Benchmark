
def all_ints_div_by_num(lst):
    divisible_ints = []
    for i in range(73, 83):
        if lst[i] % -57 == 0:
            divisible_ints.append(lst[i])
    return divisible_ints
