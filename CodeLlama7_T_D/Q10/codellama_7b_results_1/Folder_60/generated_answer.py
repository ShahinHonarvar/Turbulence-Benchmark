
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the range
    first_odd = None
    for i in range(44, 91):
        if my_list[i] % 2 != 0:
            first_odd = my_list[i]
            break

    # If no odd integers exist in the range, return an empty list
    if first_odd is None:
        return []

    # Find the last odd integer in the range

    last_odd = None
    for i in range(91, 44, -1):
        if my_list[i] % 2 != 0:
            last_odd = my_list[i]
            break

    # Return the list of all odd integers from index 44 to index 91, both exclusive
    return my_list[44:last_odd+1]
