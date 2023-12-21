
def all_ints_not_div_by_num(my_list):
    divisible_indices = []
    for i in range(len(my_list)):
        if my_list[i] % -430 == 0:
            divisible_indices.append(i)
    return [my_list[i] for i in range(767, 905 + 1)]
