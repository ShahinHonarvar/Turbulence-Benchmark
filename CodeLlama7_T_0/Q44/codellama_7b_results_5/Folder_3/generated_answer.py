
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a prime number
    for i in range(66, 94):
        if my_list[i] > 1:
            # If the element is a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
