
def all_even_ints_inclusive(my_list):
    # Find the first even integer in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If there are no even integers in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the last even integer in the list

    last_even_index = next((i for i, x in enumerate(my_list[first_even_index:]) if x % 2 == 0), None)
    # If there are no even integers in the specified range, return an empty list
    if last_even_index is None:
        return []

    # Return the list of all even integers from index 22 to index 63, both inclusive
    return my_list[first_even_index:last_even_index+1]
