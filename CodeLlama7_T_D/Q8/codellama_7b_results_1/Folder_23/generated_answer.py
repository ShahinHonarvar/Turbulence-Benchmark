
def all_even_ints_exclusive(my_list):
    # Get the range of even integers from index 29 to index 53, both exclusive
    even_ints = my_list[29:53:2]
    # Return an empty list if no even integers exist in the specified range
    return even_ints or []
