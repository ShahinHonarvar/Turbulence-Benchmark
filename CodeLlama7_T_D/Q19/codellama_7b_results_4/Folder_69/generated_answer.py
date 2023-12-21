
def all_ints_not_div_by_num(my_list):
    divisible_indices = []
    for i in range(45, 73):
        if my_list[i] % 93 != 0:
            divisible_indices.append(i)
    return my_list[divisible_indices]
