
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(28, 39):
        # Check if the current number is a composite number
        if my_list[i] > 1 and all(my_list[i] % j != 0 for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 28 and 38, inclusive
    return composite_nums
