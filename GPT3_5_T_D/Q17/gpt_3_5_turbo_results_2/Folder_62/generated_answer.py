
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(44, 60):
        if lst[i] % 39 == 0 and lst[i] % 15 == 0:
            result.append(lst[i])
    return result
