
def sum_even_ints_inclusive(nums):
    # Iterate through the list of integers and check if each element is even
    for i in range(667, 775):
        # If an even integer is found, add it to the sum
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum
