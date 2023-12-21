
def all_even_ints_exclusive(my_list):
    # Create a slice of the list from index 49 to index 74, both exclusive
    even_ints = my_list[49:74]
    # Filter out any odd integers from the slice
    even_ints = [i for i in even_ints if i % 2 == 0]
    return even_ints
