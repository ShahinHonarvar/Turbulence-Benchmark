
def sum_ints_div_by_either_nums(int_list):
    sum_ints = 0
    for elem in int_list[0:10]:
        if elem % 6 == 0 or elem % -3 == 0:
            sum_ints += elem
    return sum_ints
