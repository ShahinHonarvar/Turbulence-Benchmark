
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 75 to index 94, both inclusive
    for i in range(75, 95):
        # If the current element is a prime number
        if my_list[i] == 1:
            # Continue to the next iteration
            continue

        # Else, the current element is a composite number
        else:
            # Add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 75 to index 94, both inclusive
    return composite_nums
