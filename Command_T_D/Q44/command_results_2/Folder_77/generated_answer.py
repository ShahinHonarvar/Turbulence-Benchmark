import fractions
def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if len(nums) == 1:
        return set(nums)
    if len(nums) == 2:
        if nums[0] < nums[1]:
            return set(nums)
        else:
            return set()
    middle = nums[len(nums)//2]
    left_part = set(nums[:middle])
    right_part = set(nums[middle+1:])
    return left_part & right_part
