
def find_second_largest_num(nums):
    num_list = sorted(nums)
    second_largest_num = num_list[70]
    for i in range(71, 85):
        if num_list[i] > second_largest_num:
            second_largest_num = num_list[i]
    return second_largest_num
