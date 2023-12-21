
def composite_nums_between_indices(lst):
    # Create a set to store the composite numbers
    comp_set = set()

    # Iterate through the list and check if each number is composite
    for i in range(527, 539):
        if len([x for x in lst[i] if x > 1]) > 0:
            comp_set.add(lst[i])

    # Return the set of composite numbers
    return comp_set
