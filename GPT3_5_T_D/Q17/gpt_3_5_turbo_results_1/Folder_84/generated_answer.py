
def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(78, 82):
        if lst[i] % 76 == 0 and lst[i] % 60 == 0:
            divisible_ints.append(lst[i])
    return divisible_ints
