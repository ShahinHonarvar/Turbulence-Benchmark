
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[31:51] if x % 81 == 0 or x % 64 == 0])
