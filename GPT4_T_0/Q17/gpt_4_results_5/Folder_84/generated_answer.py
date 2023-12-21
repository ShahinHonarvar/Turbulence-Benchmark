
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(78, 82):
        if lst[i] % 76 == 0 and lst[i] % 60 == 0:
            result.append(lst[i])
    return result
