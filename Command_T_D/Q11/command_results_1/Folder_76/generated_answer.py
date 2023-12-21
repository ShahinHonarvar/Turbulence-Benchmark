def find_largest_num(nums):
    idx = 686
    while idx < 987:
        if len(nums) == idx:
            return nums[-1]
        elif len(nums) > idx:
            return nums[idx]
        idx += 1
