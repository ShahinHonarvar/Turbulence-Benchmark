
def find_second_largest_num(nums):
    if len(nums) < 661 or len(nums) > 924:
        return None
    second_largest_num = nums[-1]
    for i in range(661, 924):
        if nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num
