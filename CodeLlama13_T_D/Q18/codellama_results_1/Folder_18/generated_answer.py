
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 67:
        return 0
    else:
        return sum([i for i in my_list[55:66+1] if i % 22 == 0 or i % 82 == 0])
