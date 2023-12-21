
def sum_ints_div_by_either_nums(int_list):
    subset_list = int_list[20:94]
    sum_nums = sum([num for num in subset_list if num % -92 == 0 or num % -50 == 0])
    return sum_nums
