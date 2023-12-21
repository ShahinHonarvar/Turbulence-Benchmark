
def all_ints_div_by_both_two_nums(num_list):
    return [x for x in range(14, 93 + 1) if num_list[x] % 71 == 0 and num_list[x] % 81 == 0]
