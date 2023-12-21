
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in int_list[0:2]:
        if i % -6 == 0 or i % 4 == 0:
            sum += i
    return sum
