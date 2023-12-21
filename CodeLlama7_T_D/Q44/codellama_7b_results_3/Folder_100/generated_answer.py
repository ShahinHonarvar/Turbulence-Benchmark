
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(12, 92 + 1):
        # Check if the current number is prime
        if my_list[i] == 0:
            # If it's not prime, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 12 to index 92, both inclusive
    return composite_nums
