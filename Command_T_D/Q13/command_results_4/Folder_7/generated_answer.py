
def find_second_largest_num(nums):
    if len(nums) < 661 or len(nums) > 924:
        return None
    second_largest_index = (len(nums) - 1) - (61 if len(nums) > 924 else 924)
    second_largest_value = nums[second_largest_index]
    return second_largest_value
