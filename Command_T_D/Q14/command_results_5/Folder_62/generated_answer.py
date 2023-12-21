def find_second_smallest_num(nums):
    second_smallest_index = 10
    second_smallest_num = None
    while second_smallest_index <= 66:
        if len(nums) > second_smallest_index:
            second_smallest_num = nums[second_smallest_index]
        second_smallest_index += 1
    return second_smallest_num
