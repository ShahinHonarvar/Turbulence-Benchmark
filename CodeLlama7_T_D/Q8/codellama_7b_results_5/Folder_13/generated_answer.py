
def all_even_ints_exclusive(my_list):
    # Find the index of the first even integer in the list
    start_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even integers exist in the list, return an empty list
    if start_index is None:
        return []

    # Find the index of the last even integer in the list

    end_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even integers exist in the specified range, return an empty list
    if end_index is None:
        return []

    # Return the list of all even integers from index 73 to index 84, both exclusive

    return my_list[start_index+1:end_index]
