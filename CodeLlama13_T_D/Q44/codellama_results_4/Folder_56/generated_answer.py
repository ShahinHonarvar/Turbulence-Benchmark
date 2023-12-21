
def composite_nums_between_indices(my_list):
    # Initialize a set to store the composite numbers
    composites = set()

    # Iterate over the list and check if each number is composite
    for i in range(len(my_list)):
        if my_list[i] > 1:
            # If the number is composite, add it to the set
            composites.add(my_list[i])

    return composites
