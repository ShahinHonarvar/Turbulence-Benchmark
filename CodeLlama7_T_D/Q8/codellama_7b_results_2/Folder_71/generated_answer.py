
def all_even_ints_exclusive(my_list):
    # Find the first even index in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even indices exist in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the last even index in the list

    last_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)

    # If no even indices exist in the list, return an empty list

    if last_even_index is None:

        return []


    # Return the list of all even integers from index 36 to index 54, both exclusive

    return [my_list[i] for i in range(first_even_index + 1, last_even_index)]
