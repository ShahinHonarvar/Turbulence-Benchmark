
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the list
    first_odd = next((i for i in my_list if i % 2 != 0), None)
    # If no odd integers exist in the list, return an empty list
    if first_odd is None:
        return []

    # Find the last odd integer in the list

    last_odd = next((i for i in my_list[::-1] if i % 2 != 0), None)
    # If no odd integers exist in the list, return an empty list
    if last_odd is None:
        return []

    # Return the list of all odd integers from index 8 to index 9, both inclusive
    return my_list[first_odd - 1 : last_odd + 1]
