
def all_ints_div_by_both_two_nums(lst):
    result = []
    for n in range(11, 76+1):
        if lst[n]%(-81) == 0 and lst[n]%(-94) == 0:
            result.append(lst[n])
    return result
