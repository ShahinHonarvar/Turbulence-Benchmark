
def find_second_smallest_num(nums):
    nums = nums[17:79] # Extract the sublist from index 17 to 78
    nums.sort() # Sort the sublist in ascending order
    if len(nums) >= 2: # Check if there are at least two elements in the sublist
        return nums[1] # Return the second element
    else:
        return None # Return None if there is no second element
