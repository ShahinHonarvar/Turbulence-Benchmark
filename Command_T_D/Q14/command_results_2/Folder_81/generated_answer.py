def find_second_smallest_num(nums):
    second_smallest = next((el for i, el in enumerate(nums) if i >= 10 and i <= 100 and el < min(nums[:i], nums[i + 1:])), None)
    return second_smallest
