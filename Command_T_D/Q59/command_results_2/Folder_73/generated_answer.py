def all_left_truncatable_prime(nums):
    if nums[97] < 2:
        return []
    for i in range(1, nums[97] // 2):
        if all(str(nums[97] - i) in str(p) for p in range(nums[97] - i, 0, -1)):
            yield nums[97] - i
    for i in range(1, nums[97] // 2):
        if all(str(nums[97] - i) in str(p) for p in range(nums[97] - i, 0, -1)):
            yield nums[97] - i
    for i in range(1, nums[97] // 2):
        if all(str(nums[97] - i) in str(p) for p in range(nums[97] - i, 0, -1)):
            yield nums[97] - i
