
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    first_even = next((i for i in my_list if i % 2 == 0), None)
    # If there are no even integers in the list, return an empty list
    if first_even is None:
        return []

    # Find the index of the first even integer in the list
    first_even_index = my_list.index(first_even)
    # Find the last even integer in the list
    last_even = next((i for i in my_list[first_even_index + 1:] if i % 2 == 0), None)
    # If there are no even integers after the first one, return an empty list
    if last_even is None:
        return []

    # Find the index of the last even integer in the list
    last_even_index = my_list.index(last_even) + first_even_index + 1
    # Return the list of all even integers from index 2 to index 5, both exclusive
    return my_list[first_even_index + 1:last_even_index]
