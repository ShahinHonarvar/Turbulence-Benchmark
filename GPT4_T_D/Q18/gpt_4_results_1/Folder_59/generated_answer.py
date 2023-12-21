
def sum_ints_div_by_either_nums(num_list):
    sums = 0
    for i in range(min(9, len(num_list))):
        if num_list[i] % 8 == 0 or num_list[i] % -3 == 0:
            sums += num_list[i]
    return sums
