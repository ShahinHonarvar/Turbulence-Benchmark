
def sum_odd_ints_inclusive(nums):
    odd_numbers = [num for num in nums[8:10] if num % 2 != 0]
    return sum(odd_numbers) if odd_numbers else 0
