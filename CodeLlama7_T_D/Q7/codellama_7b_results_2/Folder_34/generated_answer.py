
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If there are no even integers in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the index of the last even integer in the list
    last_even_index = next(i for i, x in enumerate(my_list) if x % 2 == 0)

    # Return a list containing all the even integers from the specified range
    return [x for x in my_list[first_even_index:last_even_index+1] if x % 2 == 0]
