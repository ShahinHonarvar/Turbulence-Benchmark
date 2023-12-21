def find_second_smallest_num(nums):
    second_smallest = next((el for el in nums[310:370+1] if el < min(nums[310:370+1])), None)
    return second_smallest
