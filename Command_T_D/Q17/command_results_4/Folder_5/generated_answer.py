
def all_ints_div_by_both_two_nums(num_list):
    return [x for x in range(min(num_list), max(num_list) + 1) if x % 4 == 0 and x % 6 == 0]
