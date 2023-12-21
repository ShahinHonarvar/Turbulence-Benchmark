
def sum_odd_ints_inclusive(nums):
    # Use a list comprehension to find all odd integers in the range
    odd_ints = [n for n in nums[28:39] if n % 2 == 1]
    
    # If there are no odd integers, return 0
    if not odd_ints:
        return 0
    
    # Otherwise, return the sum of all odd integers
    return sum(odd_ints)
