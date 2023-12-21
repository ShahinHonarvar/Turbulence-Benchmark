
def all_ints_div_by_both_two_nums(my_list):
    divisible_indices = []
    for i in range(68, 100):
        if my_list[i] % -37 == 0 and my_list[i] % -26 == 0:
            divisible_indices.append(i)
    return divisible_indices
