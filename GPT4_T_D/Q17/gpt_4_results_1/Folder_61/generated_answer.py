
def all_ints_div_by_both_two_nums(int_list):
    divisible_list = []
    for i in int_list[0:7]:
        if i % -5 == 0 and i % -6 == 0:
            divisible_list.append(i)
    return divisible_list
