
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer
    first_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1)), None)
    # Find the index of the last odd integer
    last_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1)) - 1
    # Return the list of all odd integers from index 62 to index 96, both exclusive
    return my_list[first_odd_index:last_odd_index]
