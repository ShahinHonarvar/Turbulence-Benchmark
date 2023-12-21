
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(41, 57):
        if lst[i] % 82 == 0 and lst[i] % 90 == 0:
            result.append(lst[i])
    return result
