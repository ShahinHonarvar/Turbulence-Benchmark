
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(62, 78 + 1):
        if len(nums) > i:
            second_largest_num = nums[i - 1]
            break
    return second_largest_num
