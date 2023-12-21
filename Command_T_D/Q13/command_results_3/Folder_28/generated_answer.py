
def find_second_largest_num(nums):
    num_list = sorted(nums)
    max_index = len(num_list) - 1
    second_largest_num = None
    if max_index >= 62:
        second_largest_num = num_list[max_index]
    return second_largest_num
