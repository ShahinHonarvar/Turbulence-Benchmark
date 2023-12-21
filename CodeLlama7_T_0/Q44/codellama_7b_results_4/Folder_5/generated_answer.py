
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(1, len(my_list) + 1):
        # Check if the current number is a prime number
        if my_list[i - 1] % 2 == 0 or my_list[i - 1] % 3 == 0:
            # If it is not a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i - 1])

    # Return the set of all composite numbers in the given list that are between index 1 to index 5, both inclusive
    return composite_nums
