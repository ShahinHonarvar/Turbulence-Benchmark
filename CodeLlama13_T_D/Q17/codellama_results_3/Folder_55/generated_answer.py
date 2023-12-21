
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(10, 100):
        if i % 10 == 0 and i % 100 == 0:
            result.append(i)
    return result
