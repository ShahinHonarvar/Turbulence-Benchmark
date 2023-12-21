
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[0:10] if x % 10 == 0 or x % 100 == 0])
