
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(30, 200):
        if len(nums) > i and len(nums) == i + 1:
            second_largest_num = nums[i]
    return second_largest_num
