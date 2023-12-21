
def all_ints_div_by_both_two_nums(my_list):
    start_index = 42
    end_index = 43
    divisible_integers = []
    for i in range(start_index, end_index + 1):
        if my_list[i] % 15 == 0 and my_list[i] % 87 == 0:
            divisible_integers.append(my_list[i])
    return divisible_integers
