
def sum_even_ints_inclusive(nums):
    # Return 0 if no even integers exist in the specified range
    if not any(i % 2 == 0 for i in nums[27:56]):
        return 0
    
    # Sum all even integers from index 27 to index 55, both inclusive
    return sum(i for i in nums[27:56] if i % 2 == 0)
