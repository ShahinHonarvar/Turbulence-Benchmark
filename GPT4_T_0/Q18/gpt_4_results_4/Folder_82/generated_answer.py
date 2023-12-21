
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 201:
        return 0
    else:
        return sum(i for i in int_list[20:201] if i % -20 == 0 or i % -200 == 0)
