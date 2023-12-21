
def all_ints_div_by_both_two_nums(lst):
    divisible = []
    for i in range(13, 92):
        if lst[i] % -65 == 0 and lst[i] % -62 == 0:
            divisible.append(lst[i])
    return divisible
