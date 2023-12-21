
def all_even_ints_exclusive(my_list):
    # Get the range of even integers from index 20 to index 36, exclusive
    even_ints = [x for x in my_list[20:36] if x % 2 == 0]
    return even_ints
