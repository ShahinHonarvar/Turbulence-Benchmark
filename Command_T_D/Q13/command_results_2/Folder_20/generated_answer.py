
def find_second_largest_num(nums):
    if len(nums) < 56 or len(nums) < 66:
        return None
    second_largest_index = nums.index(sorted(nums)[56])
    return nums[second_largest_index]
