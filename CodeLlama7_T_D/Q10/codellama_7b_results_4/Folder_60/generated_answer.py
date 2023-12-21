
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer in the list
    first_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1)), None)
    # If no odd integers exist in the specified range, return an empty list
    if first_odd_index is None:
        return []

    # Return the list of all odd integers from index 44 to index 91, both exclusive
    return my_list[first_odd_index + 1 : 91]
