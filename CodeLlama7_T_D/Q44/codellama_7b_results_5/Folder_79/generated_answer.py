
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the indices of the given list
    for i in range(6, len(my_list) + 1):
        # Check if the number at the current index is composite
        if my_list[i - 1] > 1 and any(my_list[i - 1] % x == 0 for x in range(2, int(my_list[i - 1]) ** 0.5 + 1))):
            # If it is composite, add it to the set of composite numbers
            composite_nums.add(my_list[i - 1])
    return composite_nums
