
def all_ints_not_div_by_num(my_list):
    divisible_indices = []
    for i in range(20, 51):
        if my_list[i] % -48 != 0:
            divisible_indices.append(i)
    return my_list[divisible_indices]
