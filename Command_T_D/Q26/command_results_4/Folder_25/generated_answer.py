def sum_in_range(nums):
    result = 0
    for i in nums:
        if -10 <= i <= 48:
            result += i
    return result
