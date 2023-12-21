
def composite_nums_between_indices(my_list):
    # Create a set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is composite
    for i in range(43, 87):
        if my_list[i] > 1:
            # If an element is composite, add it to the set
            composite_nums.add(my_list[i])

    return composite_nums
