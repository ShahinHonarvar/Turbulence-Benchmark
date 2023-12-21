def all_odd_ints_exclusive(nums):
    odds = [i for i in range(57, 85, 2) if i in nums]
    return [i for i in range(57, 85, 2) if i not in nums] if odds else []
