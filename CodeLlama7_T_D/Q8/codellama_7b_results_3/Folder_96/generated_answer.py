
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list, starting from index 50
    for i in range(50, len(my_list)):
        if my_list[i] % 2 == 0:
            first_even_index = i
            break

    # If no even integers exist in the specified range, return an empty list.
    if first_even_index is None:
        return []

    # Find the last even integer in the list, starting from index 200.
    for i in range(first_even_index, 200):
        if my_list[i] % 2 == 0:
            last_even_index = i
            break

    # Return the list of all even integers from index 50 to index 200, both exclusive.
    return my_list[first_even_index + 1 : last_even_index]
