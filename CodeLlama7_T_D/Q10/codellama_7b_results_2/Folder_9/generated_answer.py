
def all_odd_ints_exclusive(my_list):
    # Get the indices of the first and last odd integers in the list
    first_odd = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    last_odd = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    # If no odd integers exist in the list, return an empty list
    if first_odd is None or last_odd is None:
        return []

    # Return the list of all odd integers from index 70 to index 71, both exclusive
    return my_list[first_odd + 1 : last_odd]
