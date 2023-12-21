
def all_ints_not_div_by_num(my_list):
    divisible_inds = []
    for i in range(8, len(my_list)):
        if my_list[i] % -3 == 0:
            divisible_inds.append(i)
    return [my_list[i] for i in range(8, len(my_list))) if i not in divisible_inds]
