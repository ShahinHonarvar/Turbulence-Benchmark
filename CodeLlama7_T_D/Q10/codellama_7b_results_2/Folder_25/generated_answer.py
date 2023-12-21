
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the list
    first_odd = None
    for i in range(41, len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd = i
            break

    # If no odd integers exist in the specified range, return an empty list
    if first_odd is None:
        return []

    # Find the last odd integer in the list

    last_odd = None

    for i in range(first_odd, len(my_list)):
        if my_list[i] % 2 != 0:
            last_odd = i

    # Return the list of all odd integers from index 41 to index 69, both exclusive

    return my_list[first_odd:last_odd+1]
