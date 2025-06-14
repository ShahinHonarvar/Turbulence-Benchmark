
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list, starting from index 20
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If there are no even integers in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the last even integer in the list, starting from index 200
    last_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0)), None)
    # If there are no even integers in the list, return an empty list
    if last_even_index is None:
        return []

    # Return the list of all even integers from index 20 to index 200, both exclusive
    return my_list[first_even_index + 1 : last_even_index]
