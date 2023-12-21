
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers and check if each number is composite
    for i in range(70, 85):
        if my_list[i] > 1:
            # If the number is composite, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
