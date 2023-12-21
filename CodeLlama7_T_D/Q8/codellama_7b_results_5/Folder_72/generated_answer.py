
def all_even_ints_exclusive(my_list):
    # Get the indices of the first and last even integers in the list
    first_even = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    last_even = next((i for i, x in enumerate(my_list) if x % 2 == 0)), None)
    # Check if there are any even integers in the specified range
    if first_even is not None and last_even is not None:
        # Return the list of all even integers from index 56 to index 88, both exclusive
        return [my_list[i] for i in range(first_even + 1, last_even)]
    else:
        # Return an empty list if no even integers exist in the specified range
        return []
