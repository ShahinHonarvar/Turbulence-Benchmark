def composite_nums_between_indices(nums):
    if 28 <= len(nums) <= 40:
        return {num for num in nums[28:40+1] if num > 1 and num % 2 == 0 and num % 3 == 0 and num % 5 == 0 and num % 7 == 0 and num % 11 == 0 and num % 13 == 0 and num % 17 == 0 and num % 19 == 0 and num % 23 == 0 and num % 29 == 0 and num % 31 == 0 and num % 37 == 0 and num % 41 == 0}
    else:
        return set()
