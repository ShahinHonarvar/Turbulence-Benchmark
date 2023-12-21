
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[38:53]
    sum_ = sum(filter(lambda x: x % -41 == 0 or x % -47 == 0, sub_list))
    return sum_ if sum_ else 0
