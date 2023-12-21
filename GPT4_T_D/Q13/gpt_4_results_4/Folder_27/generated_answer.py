
def find_second_largest_num(nums):
    if len(nums) < 94:
        return None
    else:
        return sorted(nums[66:94])[-2]
