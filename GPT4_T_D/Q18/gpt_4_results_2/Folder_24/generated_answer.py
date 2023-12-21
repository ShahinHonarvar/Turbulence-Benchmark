
def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for i in range(29, 54):
        if i < len(num_list):
            if num_list[i] % -68 == 0 or num_list[i] % -85 == 0:
                sum += num_list[i]

    return sum
