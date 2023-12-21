
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(100, len(nums) + 1):
        if len(nums) - i < 200:
            second_largest_num = max(nums[i:])
    return second_largest_num
