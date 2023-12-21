
def find_second_largest_num(nums):
    second_largest = -1
    for i in range(59, 97):
        if len(nums) >= i:
            second_largest = max(second_largest, nums[i])
    return second_largest
