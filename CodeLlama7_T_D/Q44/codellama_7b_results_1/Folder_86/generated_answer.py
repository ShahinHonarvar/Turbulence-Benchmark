
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last composite numbers in the list
    first_composite = next((i for i, x in enumerate(my_list) if is_composite(x)), None)
    last_composite = next((i for i, x in enumerate(reversed(my_list))) if is_composite(x)), None)
    # If no composite numbers exist in the specified range, return an empty set
    if first_composite is None or last_composite is None:
        return set()

    # Return the set of all composite numbers between the first and last composite numbers in the list

    return set(my_list[first_composite:last_composite+1])
