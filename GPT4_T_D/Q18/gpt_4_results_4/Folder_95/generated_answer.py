
def sum_ints_div_by_either_nums(num_list):
    total_sum = 0
    for i in range(57, 85):
        try:
            if num_list[i] % -30 == 0 or num_list[i] % -88 == 0:
                total_sum += num_list[i]
        except IndexError:
            break
    return total_sum
