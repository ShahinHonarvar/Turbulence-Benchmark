
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the elements in the given list
    for i in range(55, 98 + 1):
        # Check if the current element is a prime number
        if my_list[i] > 1:
            # If it is a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    # Return the set of composite numbers in the specified range
    return composite_nums
