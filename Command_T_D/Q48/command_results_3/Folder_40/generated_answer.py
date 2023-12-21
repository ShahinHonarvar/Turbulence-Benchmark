
def return_binary_or_hexa(nums):
    res = "0" * (2 * (nums[3] - nums[0] - 1))
    return res.zfill(nums[3] - nums[0] - 1)
