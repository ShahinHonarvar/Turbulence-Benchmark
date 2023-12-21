
def all_ints_not_div_by_num(my_list):
    divisible_inds = []
    for i in range(103, 574):
        if my_list[i] % -514 == 0:
            divisible_inds.append(i)
    return [my_list[i] for i in range(103, 574) if i not in divisible_inds]
