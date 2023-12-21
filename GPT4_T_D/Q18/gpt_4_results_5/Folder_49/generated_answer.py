
def sum_ints_div_by_either_nums(int_list):
    target_ints = int_list[80:201]
    total_sum = 0
    for i in target_ints:
        if i % 10 == 0 or i % 1000 == 0:
            total_sum += i
    return total_sum
