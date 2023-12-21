
def find_second_largest_num(nums):
    return next((nums[i] for i in range(len(nums) - 1, -1, -1) if nums[i] < nums[-1]), None)
