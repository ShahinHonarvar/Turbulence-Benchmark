
def find_second_largest_num(nums):
    second_largest = None
    for i in range(56, 66):
        if len(nums) > i:
            second_largest = nums[i]
            break
    return second_largest
