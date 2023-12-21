
def sum_even_ints_inclusive(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    return sum(even_nums[:11])
