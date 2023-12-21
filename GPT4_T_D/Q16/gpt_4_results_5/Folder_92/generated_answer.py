
def sum_even_ints_inclusive(nums):
    subset = nums[:2]
    return sum(num for num in subset if num % 2 == 0)
