
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 81:
        return 0
    else:
        return sum([x for x in my_list[78:82] if x % 76 == 0 or x % 60 == 0])
