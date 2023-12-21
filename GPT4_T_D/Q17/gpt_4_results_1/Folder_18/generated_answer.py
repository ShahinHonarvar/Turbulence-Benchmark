
def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(55, 67):
        if lst[i] % 22 == 0 and lst[i] % 82 == 0:
            divisible_ints.append(lst[i])
    return divisible_ints
