
def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(58, 81):
        if (i % 55 == 0) and (i % 10 == 0):
            result.append(i)
    return result
