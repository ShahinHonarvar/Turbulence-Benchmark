
def sum_ints_div_by_either_nums(int_list):
    total = 0
    for integer in int_list[51:77]:
        if integer % -90 == 0 or integer % -59 == 0:
            total += integer
    return total if total else 0
