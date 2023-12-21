
def find_second_largest_num(nums):
    if not nums:
        return None
    n = len(nums)
    x = y = z = None
    for i in range(17, n - 1):
        if nums[i] > x:
            x = nums[i]
        elif nums[i] > y:
            y = nums[i]
        elif nums[i] > z:
            z = nums[i]
    return y if y else z
