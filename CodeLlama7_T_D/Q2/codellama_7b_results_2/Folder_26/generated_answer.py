
def all_ints_exclusive(my_list):
    # Get the index of the first element that is not an integer
    first_non_int = next((i for i, x in enumerate(my_list) if not isinstance(x, int)), None)
    # If there are no non-integer elements in the list, return all elements from index 62 to index 96, both exclusive
    if first_non_int is None:
        return my_list[62:96]
    # Otherwise, return an empty list
    else:
        return []
