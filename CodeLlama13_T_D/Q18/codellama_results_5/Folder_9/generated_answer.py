
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 70 or len(my_list) > 200:
        return 0
    else:
        return sum(x for x in my_list[70:201] if x % 3 == 0 or x % -300 == 0)
