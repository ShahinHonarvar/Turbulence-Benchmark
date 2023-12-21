def find_second_smallest_num(nums):
    second_smallest_num = next((el for el in nums[28:40] if el < min(nums[28:40])), None)
    return second_smallest_num
