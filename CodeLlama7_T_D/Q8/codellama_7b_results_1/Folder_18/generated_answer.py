
def all_even_ints_exclusive(my_list):
    # Get the range of even integers from index 57 to index 84, both exclusive
    even_ints = my_list[57::2]
    # Return an empty list if no even integers exist in the specified range
    return even_ints or []
