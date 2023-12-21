
def sum_ints_div_by_either_nums(my_list):
    start = 42
    end = 87
    divisible_sum = 0

    for i in range(start, end + 1):
        if my_list[i] % -90 == 0 or my_list[i] % -74 == 0:
            divisible_sum += my_list[i]

    return divisible_sum
