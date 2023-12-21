def find_second_smallest_num(nums):
    result = next((nums[i] for i in range(15, 40) if i == len(nums) - 1 or nums[i] < nums[i + 1]), None)
    return result
