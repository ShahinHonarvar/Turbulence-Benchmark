
def all_odd_ints_inclusive(my_list):
    # Get the indices of the first and last odd integers in the list
    first_idx = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    last_idx = next((i for i, x in enumerate(my_list[::-1]) if x % 2 == 1), None)
    # Return the list of all odd integers from index 4 to index 8, both inclusive
    return my_list[first_idx:last_idx+1]
