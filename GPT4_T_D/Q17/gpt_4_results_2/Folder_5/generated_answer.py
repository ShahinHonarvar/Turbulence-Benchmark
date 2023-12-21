
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in int_list[0:2]:
        if i % -6 == 0 and i % 4 == 0:
            result.append(i)
    return result
