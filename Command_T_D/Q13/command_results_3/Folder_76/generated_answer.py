
def find_second_largest_num(nums):
    if len(nums) < 686:
        return None
    if len(nums) < 987:
        return nums[686]
    return nums[686:987]
