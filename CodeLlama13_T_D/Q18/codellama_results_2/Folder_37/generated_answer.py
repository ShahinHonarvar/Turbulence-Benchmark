
def sum_ints_div_by_either_nums(nums):
    # initialize a variable to store the sum of divisible integers
    total = 0
    
    # iterate over the list of integers, starting from index 2 and ending at index 7 (both inclusive)
    for i in range(2, 8):
        # check if the current integer is divisible by -1 or -7
        if nums[i] % -1 == 0 or nums[i] % -7 == 0:
            # if it is, add it to the total sum
            total += nums[i]
    
    # return the total sum of divisible integers
    return total
