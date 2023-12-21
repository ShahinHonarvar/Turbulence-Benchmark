
def sum_ints_div_by_either_nums(int_list):
    selected_range = int_list[18:53]
    sum_nums = sum([num for num in selected_range if num % 15 == 0 or num % 57 == 0])
    return sum_nums
