
def find_second_largest_num(nums):
    second_largest = None
    for i in range(90, len(nums) + 1, 1):
        second_largest = max(second_largest, nums[i])
    return second_largest
