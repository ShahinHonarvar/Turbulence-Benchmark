
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer in the list
    first_even_index = None
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            first_even_index = i
            break

    # If no even integers exist in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the index of the last even integer in the list
    last_even_index = None
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] % 2 == 0:
            last_even_index = i
            break

    # If no even integers exist in the list, return an empty list
    if last_even_index is None:
        return []

    # Return a list of all even integers from index 75 to index 85, both inclusive
    return my_list[first_even_index:last_even_index+1]
