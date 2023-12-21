
def all_ints_not_div_by_num(nums_list):
    range_elements = nums_list[39:81]
    return [num for num in range_elements if num % 49 != 0]
