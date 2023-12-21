
def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for x in int_list[299:383]:
        if x % 858 == 0 or x % 952 == 0:
            total_sum += x
    return total_sum
