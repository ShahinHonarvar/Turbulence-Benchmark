
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer in the list
    start_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # Find the index of the last even integer in the list
    end_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # Return an empty list if no even integers exist in the specified range
    if start_index is None or end_index is None:
        return []

    # Return a list of all even integers from index 13 to index 68, both inclusive
    return [x for x in my_list[start_index:end_index+1] if x % 2 == 0]
