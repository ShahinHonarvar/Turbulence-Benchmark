
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(25, 87):
        if len(nums) > i:
            second_largest_num = nums[i]
            break
    return second_largest_num
