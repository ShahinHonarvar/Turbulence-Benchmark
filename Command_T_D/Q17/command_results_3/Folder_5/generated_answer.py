
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(0, len(lst)):
        if lst[i]%4 == 0 and lst[i]%(-6) == 0:
            result.append(lst[i])
    return result
