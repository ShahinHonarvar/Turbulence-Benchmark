
def sum_even_ints_inclusive(nums):
    evens = [num for num in nums[70:201] if num % 2 == 0]
    return sum(evens) if evens else 0
