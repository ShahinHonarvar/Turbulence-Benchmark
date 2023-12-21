
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(299, 382):
        if lst[i] % 858 == 0 and lst[i] % 952 == 0:
            result.append(i)
    return result
