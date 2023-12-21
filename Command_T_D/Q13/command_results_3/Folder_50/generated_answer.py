
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(70, 85):
        if len(nums) > i:
            second_largest_num = nums[i]
            break
    return second_largest_num
