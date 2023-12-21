
def all_odd_ints_exclusive(nums):
    odd_ints = []
    for i in range(43, 99):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints
