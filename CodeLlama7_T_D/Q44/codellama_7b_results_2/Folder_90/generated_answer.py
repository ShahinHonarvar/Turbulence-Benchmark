
def composite_nums_between_indices(my_list):
    # Check if my_list is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers.")
    # Find the indices of the first and last composite numbers in the list
    first_composite = None
    last_composite = None
    for i, n in enumerate(my_list):
        if is_composite(n):
            if first_composite is None:
                first_composite = i

            last_composite = i

    # Return the set of all composite numbers between the first and last indices
    return set(my_list[first_composite:last_composite+1])
