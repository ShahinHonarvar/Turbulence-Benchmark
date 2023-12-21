
def composite_nums_between_indices(my_list):
    # Find the starting and ending indices of the range
    start = 75
    end = 94
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list from the starting index to the ending index
    for i in range(start, end + 1):
        # Check if the current number is a prime number
        if my_list[i] == 1:
            # If it's a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    # Return the set of composite numbers in the specified range
    return composite_nums
