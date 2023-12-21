
def all_odd_ints_inclusive(my_list):
    # Find the first and last odd indices in the list
    first_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    last_odd_index = next((i for i, x in enumerate(my_list[::-1]) if x % 2 == 1), None)
    # If there are no odd indices in the list, return an empty list
    if first_odd_index is None and last_odd_index is None:
        return []

    # Return the list of all odd integers from index 43 to index 86, both inclusive
    return [my_list[i] for i in range(first_odd_index, last_odd_index + 1)]
