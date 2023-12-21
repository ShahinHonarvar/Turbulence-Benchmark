
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[69:98]
    total_sum = 0
    for i in subset:
        if i % -90 == 0 or i % -67 == 0:
            total_sum += i
    return total_sum
