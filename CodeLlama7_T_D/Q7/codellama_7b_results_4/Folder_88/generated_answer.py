
def all_even_ints_inclusive(my_list):
    # Get the range of even integers from index 4 to index 8, both inclusive
    even_int_range = [x for x in my_list[4:9] if x % 2 == 0]
    return even_int_range
