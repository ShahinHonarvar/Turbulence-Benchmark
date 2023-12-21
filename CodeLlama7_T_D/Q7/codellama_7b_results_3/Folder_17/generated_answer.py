
def all_even_ints_inclusive(my_list):
    # Find the first even index in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even integers exist in the specified range, return an empty list
    if first_even_index is None:
        return []

    # Find the last even index in the list

    last_even_index = next(i for i in range(first_even_index + 1, len(my_list)) if my_list[i] % 2 == 0), None)
    # If no even integers exist in the specified range, return an empty list
    if last_even_index is None:
        return []

    # Return a list of all even integers from index 62 to index 78, both inclusive
    return [my_list[i] for i in range(first_even_index, last_even_index + 1)]
