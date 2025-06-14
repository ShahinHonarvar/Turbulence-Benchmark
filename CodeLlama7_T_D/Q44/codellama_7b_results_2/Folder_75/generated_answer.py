
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Loop through the indices in the range [75, 85]
    for i in range(75, 86):
        # Check if the current number is prime
        if my_list[i] == 1 or any(my_list[i] % j == 0 and j < my_list[i] for j in range(2, int(my_list[i] ** 0.5) + 1))):
            # If it is prime, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    return composite_nums
