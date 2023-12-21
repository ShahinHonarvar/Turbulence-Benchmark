def all_odd_ints_inclusive(nums):
    result = []
    for num in nums[686:987]:
        if num % 2 == 1:
            result.append(num)
    return result
