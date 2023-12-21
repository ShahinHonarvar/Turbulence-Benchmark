
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 75:
        return 0
    
    return sum(x for x in my_list[58:76] if x % 72 == 0 or x % 62 == 0)
