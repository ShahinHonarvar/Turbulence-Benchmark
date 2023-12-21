
def all_even_ints_exclusive(my_list):
    # Get the range of even integers from index 40 to index 200, both exclusive
    even_ints = my_list[40:200:2]
    # Return an empty list if no even integers exist in the specified range
    return even_ints if even_ints else []
