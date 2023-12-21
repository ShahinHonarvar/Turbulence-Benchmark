def find_second_smallest_num(nums):
    second_smallest_num = next((x for x in nums[34:55] if x < min(nums[34:55])), None)
    return second_smallest_num
