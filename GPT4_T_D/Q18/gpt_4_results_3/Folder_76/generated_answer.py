
def sum_ints_div_by_either_nums(int_list):
    relevant_range = int_list[250:630]
    sum_nums = sum(i for i in relevant_range if i % 850 == 0 or i % 587 == 0)
    return sum_nums
