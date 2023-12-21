def find_second_smallest_num(nums):
    second_smallest_num = nums[26]
    while second_smallest_num in nums[26:]:
        second_smallest_num += 1
    return second_smallest_num
