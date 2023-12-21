
def sum_even_ints_inclusive(nums):
    sum_even = sum(num for idx, num in enumerate(nums[13:69]) if num % 2 == 0)
    return sum_even if sum_even else 0
