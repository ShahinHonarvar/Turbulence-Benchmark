
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is composite
    for i in range(26, 53):
        # If the number is not prime, add it to the set of composite numbers
        if my_list[i] > 1:
            composite_nums.add(my_list[i])

    # Return the set of composite numbers between indices 26 and 52
    return composite_nums
