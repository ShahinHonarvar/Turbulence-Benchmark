
def all_ints_div_by_num(my_list):
    start_index = 66
    end_index = 74
    divisible_integers = []
    for i in range(start_index, end_index + 1):
        if my_list[i] % -14 == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
