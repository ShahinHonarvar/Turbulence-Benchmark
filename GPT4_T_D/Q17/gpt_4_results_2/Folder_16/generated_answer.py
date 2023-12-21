
def all_ints_div_by_both_two_nums(lst):
    divisible_integers = []
    for i in range(55, 81):
        if lst[i] % 22 == 0 and lst[i] % 32 == 0:
            divisible_integers.append(lst[i])
    return divisible_integers
