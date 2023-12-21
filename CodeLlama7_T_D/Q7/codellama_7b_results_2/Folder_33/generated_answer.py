
def all_even_ints_inclusive(my_list):
    # Find the first even index in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If there are no even indices in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the last even index in the list

    last_even_index = next((i for i, x in enumerate(my_list[first_even_index:]) if x % 2 == 0), None)
    # If there are no even indices in the specified range, return an empty list
    if last_even_index is None:
        return []

    # Return a list of all even integers from index 667 to index 774, both inclusive

    return [my_list[i] for i in range(first_even_index, last_even_index + 1)]
