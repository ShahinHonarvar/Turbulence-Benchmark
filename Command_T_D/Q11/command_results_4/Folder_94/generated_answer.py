def find_largest_num(nums):
    largest = max(nums[28:40] + [nums[40]], key=lambda x: x)
    return largest
