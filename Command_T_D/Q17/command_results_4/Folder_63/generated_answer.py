
def all_ints_div_by_both_two_nums(l):
    return [i for i in range(31, 51) if l[i] % 64 == 0 and l[i] % 81 == 0]
