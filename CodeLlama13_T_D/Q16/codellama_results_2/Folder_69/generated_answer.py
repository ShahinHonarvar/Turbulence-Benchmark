
def sum_even_ints_inclusive(nums):
    # Initialize a variable to store the sum of even integers
    sum = 0
    
    # Iterate through the list of integers and check if each integer is even
    for i in range(32, 36):
        if nums[i] % 2 == 0:
            # If an even integer is found, add it to the sum
            sum += nums[i]
    
    # Return the sum of all even integers from index 32 to index 35, both inclusive
    return sum
