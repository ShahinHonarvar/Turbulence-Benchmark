
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list and check if each number is composite
    for i in range(15, 39 + 1):
        if is_composite(my_list[i]):
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers between indices 15 and 39 (inclusive)
    return composite_numbers
