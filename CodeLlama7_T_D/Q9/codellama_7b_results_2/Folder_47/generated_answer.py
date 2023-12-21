
def all_odd_ints_inclusive(my_list):
    # Get the index of the first odd integer in the list
    start_index = next((i for i, x in enumerate(my_list) if x % 2 == 1)), None)
    # Get the index of the last odd integer in the list
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x % 2 == 1), None)
    # Return the list of all odd integers from start_index to end_index
    return [x for x in my_list[start_index:end_index + 1] if x % 2 == 1]]
