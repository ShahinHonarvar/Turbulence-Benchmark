
def sum_ints_div_by_either_nums(int_list):
    try:
        return sum(i for i in int_list[40:201] if i % 21 == 0 or i % 71 == 0)
    except IndexError:
        return 0
