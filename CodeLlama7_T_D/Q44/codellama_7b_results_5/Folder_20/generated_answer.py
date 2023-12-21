
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last composite numbers in the list
    first_composite = None
    for i in range(len(my_list)):
        if is_composite(my_list[i]):
            first_composite = i
            break

    last_composite = None
    for i in range(len(my_list) - 1, -1, -1):
        if is_composite(my_list[i]):
            last_composite = i
            break

    # Return the set of composite numbers between the indices
    return { my_list[i] for i in range(first_composite, last_composite + 1) if is_composite(my_list[i]) }
