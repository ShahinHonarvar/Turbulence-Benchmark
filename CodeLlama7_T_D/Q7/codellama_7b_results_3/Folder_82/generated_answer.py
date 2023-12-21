
def all_even_ints_inclusive(my_list):
    # Get the indices of the first and last even integers in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    last_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0)), len(my_list) - 1)
    # Return the list of all even integers from index 20 to index 200, both inclusive
    return [x for x in my_list[first_even_index:last_even_index + 1] if x % 2 == 0]
