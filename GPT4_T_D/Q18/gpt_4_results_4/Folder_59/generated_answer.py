
def sum_ints_div_by_either_nums(int_list):
    sum_ = 0
    for i in range(min(len(int_list), 9)):
        if int_list[i] % -3 == 0 or int_list[i] % 8 == 0:
            sum_ += int_list[i]
    return sum_
