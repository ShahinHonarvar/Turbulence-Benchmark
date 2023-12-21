def all_odd_ints_exclusive(nums):
    if len(nums) < 80:
        return []
    left_len = 80 - len(nums)
    right_len = 200 - len(nums)
    return nums[left_len:left_len+right_len]
