
def sum_odd_ints_inclusive(nums):
    odds = [num for num in nums[12:93] if num % 2 != 0]
    return sum(odds) if odds else 0
