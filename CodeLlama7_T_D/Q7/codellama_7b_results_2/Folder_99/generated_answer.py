
def all_even_ints_inclusive(my_list):
    # Find the first even integer in the range
    start_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If there are no even integers in the range, return an empty list
    if start_index is None:
        return []

    # Find the last even integer in the range

    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x % 2 == 0), None)
    # If there are no even integers in the range, return an empty list
    if end_index is None:
        return []

    # Return the list of all even integers from index 310 to index 370, both inclusive

    return my_list[start_index:end_index+1]
