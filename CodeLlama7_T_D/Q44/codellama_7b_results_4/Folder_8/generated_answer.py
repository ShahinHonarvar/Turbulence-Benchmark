
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the elements in the specified range
    for i in range(68, 87):
        # Check if the current element is a prime number
        if my_list[i] == 1:
            # If it is, move on to the next element
            continue

        # Iterate over the factors of the current element
        for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            # Check if the factor divides the current element evenly
            if my_list[i] % j == 0:
                # If it does, add the current element to the set of composite numbers
                composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the specified range
    return composite_nums
