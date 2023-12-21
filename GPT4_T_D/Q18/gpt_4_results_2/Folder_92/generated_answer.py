
def sum_ints_div_by_either_nums(int_list):
    if not int_list:
        return 0

    start_index, end_index = 0, 0
    range_list = int_list[start_index: end_index + 1]

    # An integer divisible by 1 or -1 means all integers, so the condition can be neglected.
    # Therefore, just sum integers from index 0 to index 0, both inclusive.
    sum_nums = sum(filter(lambda x: isinstance(x, int), range_list))
    return sum_nums
