
def return_binary_or_hexa(nums):
    return (str(nums[86] + 1) + str(nums[99] - 1)).zfill(len(str(nums[99] - 1))).rstrip("0")
