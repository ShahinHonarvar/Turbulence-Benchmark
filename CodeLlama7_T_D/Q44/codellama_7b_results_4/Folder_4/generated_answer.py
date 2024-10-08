
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is composite
    for i in range(56, 99 + 1):
        # If the number is not prime, it is a composite number
        if my_list[i] > 1:
            # Add the composite number to the set
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 56 to index 98, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_nums
