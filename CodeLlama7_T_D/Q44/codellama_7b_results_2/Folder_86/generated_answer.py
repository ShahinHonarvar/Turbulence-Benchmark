
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the elements of the input list
    for i in range(43, 87):
        # Check if the current element is prime
        if my_list[i] == 1:
            continue

        # Iterate over the factors of the current element
        for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            # Check if the current factor is a factor of the current element
            if my_list[i] % j == 0:
                # Add the current element to the set of composite numbers
                composite_nums.add(my_list[i])
                break

    return composite_nums
