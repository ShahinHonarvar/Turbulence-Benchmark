
def all_ints_div_by_both_two_nums(my_list):
    divisible_indices = []
    for i in range(281, 695):
        if my_list[i] % -722 == 0 and my_list[i] % -731 == 0:
            divisible_indices.append(i)
    return my_list[divisible_indices]
