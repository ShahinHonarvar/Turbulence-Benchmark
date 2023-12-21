
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the list and check if each number is composite
    for i in range(70, 201):
        if my_list[i] > 1:
            # If the number is composite, add it to the set
            composite_numbers.add(my_list[i])

    return composite_numbers
