
def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(10, 29):
        if lst[i] % -61 == 0 and lst[i] % -64 == 0:
            divisible_ints.append(lst[i])
    return divisible_ints
