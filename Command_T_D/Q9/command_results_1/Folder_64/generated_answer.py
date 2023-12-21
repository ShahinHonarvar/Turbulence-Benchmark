def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(len(nums) - 1):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
            odds.append(nums[i + 1])
            break
    return odds
