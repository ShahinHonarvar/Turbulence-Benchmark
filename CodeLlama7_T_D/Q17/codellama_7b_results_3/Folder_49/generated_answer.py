
def all_ints_div_by_both_two_nums(my_list):
    divisible_indices = []
    for i in range(80, 201):
        if my_list[i] % 10 == 0 and my_list[i] % 1000 == 0:
            divisible_indices.append(i)
    return my_list[divisible_indices]
