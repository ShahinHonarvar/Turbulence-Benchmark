
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 76:
        return 0
    else:
        return sum([x for x in my_list[51:77] if x % -90 == 0 or x % -59 == 0])
