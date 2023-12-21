
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the list
    first_odd = next((i for i in my_list if i % 2 != 0), None)
    # If no odd integers exist in the list, return an empty list
    if first_odd is None:
        return []

    # Find the index of the first odd integer

    first_odd_index = my_list.index(first_odd)

    # Find the last index of the odd integers

    last_odd_index = my_list[first_odd_index:].index(first_odd) + first_odd_index

    # Return the list of all odd integers between the specified indices, exclusive

    return [i for i in my_list[first_odd_index:last_odd_index] if i % 2 != 0]
