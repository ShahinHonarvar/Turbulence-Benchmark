
def all_odd_ints_exclusive(my_list):
    # Get the indices of the first and last odd integers in the list
    first_odd = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    last_odd = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    # Check if there are any odd integers in the list
    if first_odd is not None and last_odd is not None:
        # Get the range of indices that correspond to the odd integers
        odd_indices = range(first_odd, last_odd + 1)
        # Return the list of all odd integers in the specified range
        return [my_list[i] for i in odd_indices]
    else:
        # If there are no odd integers in the list, return an empty list
        return []
