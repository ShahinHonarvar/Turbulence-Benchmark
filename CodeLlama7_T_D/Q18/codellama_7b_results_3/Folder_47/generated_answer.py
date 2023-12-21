
def sum_ints_div_by_either_nums(my_list):
    start_index = 42
    end_index = 87
    divisible_ints = []

    for i in range(start_index, end_index + 1):
        if my_list[i] % -90 == 0 or my_list[i] % -74 == 0:
            divisible_ints.append(my_list[i])

    return sum(divisible_ints)
