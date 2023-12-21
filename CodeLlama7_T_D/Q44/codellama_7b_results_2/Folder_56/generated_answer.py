
def composite_nums_between_indices(my_list):
    # Find the first and last indices of the list that are greater than 1
    first_index = next((i for i, x in enumerate(my_list) if x > 1)), None)
    last_index = len(my_list) - next((i for i, x in reversed(enumerate(my_list)) if x > 1)), None)
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the range of indices that are greater than 1
    for i in range(first_index, last_index + 1):
        # Check if the number at the current index is prime
        if my_list[i] > 1:
            # If it is prime, check if any of its factors are in the list
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    # If a factor is found, add the number to the set of composite numbers
                    composite_numbers.add(my_list[i])
                    # Break out of the inner loop since we have found a factor
                    break

    # Return the set of all composite numbers in the given list that are between index 0 to index 0, both inclusive
    return composite_numbers
