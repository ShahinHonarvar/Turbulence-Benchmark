
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list from index 686 to index 987, both inclusive
    for i in range(686, 987 + 1):
        # Check if the current element is a prime number
        if my_list[i] == 0:
            # If it is not a prime number, then it is a composite number
            composite_numbers.add(my_list[i])

    return composite_numbers
