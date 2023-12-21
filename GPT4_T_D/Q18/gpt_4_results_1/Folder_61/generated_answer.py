
def sum_ints_div_by_either_nums(int_list):
    sum_val = 0
    for i in int_list[:7]:
        if i % -5 == 0 or i % -6 == 0:
            sum_val += i
    return sum_val
