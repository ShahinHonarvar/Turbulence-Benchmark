
def all_even_ints_exclusive(my_list):
    # Get the indices of the first and last even integers
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    last_even_index = next((i for i, x in enumerate(my_list[::-1]) if x % 2 == 0), None)
    # If there are no even integers in the list, return an empty list
    if first_even_index is None or last_even_index is None:
        return []

    # Get the range of indices for the even integers

    even_indices = range(first_even_index + 1, last_even_index)

    # Return the list of all even integers in the specified range

    return [my_list[i] for i in even_indices]
