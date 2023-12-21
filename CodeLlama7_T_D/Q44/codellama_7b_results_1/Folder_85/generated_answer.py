
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is composite
    for i in range(3, 6):
        if my_list[i] > 1:
            # If the number is composite, add it to the set
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 3 and 5
    return composite_nums
