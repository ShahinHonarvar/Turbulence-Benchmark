
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # Find the index of the last even integer
    last_even_index = next((i for i, x in enumerate(my_list[::-1]) if x % 2 == 0), None)
    # Return an empty list if no even integers exist in the specified range
    if first_even_index is None or last_even_index is None:
        return []

    # Return the list of all even integers from index 14 to index 64, both inclusive
    return [my_list[i] for i in range(first_even_index, last_even_index + 1)]
