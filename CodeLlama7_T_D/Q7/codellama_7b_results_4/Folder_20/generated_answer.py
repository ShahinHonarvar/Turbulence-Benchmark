
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer in the list
    first_even_index = None
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            first_even_index = i
            break

    # If no even integers exist in the specified range, return an empty list

    if first_even_index is None:
        return []

    # Return the list of all even integers from index 56 to index 66, both inclusive

    return [my_list[i] for i in range(first_even_index, min(len(my_list), 66)) if my_list[i] % 2 == 0]]
