def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
            break
    return odds
