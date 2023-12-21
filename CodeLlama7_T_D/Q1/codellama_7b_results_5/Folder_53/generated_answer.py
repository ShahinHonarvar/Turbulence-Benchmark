
def all_ints_inclusive(my_list):
    # Get the indices of the first and last elements in the list
    first_index = my_list.index(my_list[0])
    last_index = my_list.index(my_list[-1])
    # Create a new list with all elements from index 200 to index 200, both inclusive
    return my_list[first_index:last_index+1]
