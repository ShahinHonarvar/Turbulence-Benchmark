
def all_even_ints_exclusive(my_list):
    # Get the range of even integers from index 56 to index 88, both exclusive
    even_int_range = list(filter(lambda x: x % 2 == 0 and (x >= 56 and x < 88), my_list)))
    return even_int_range
