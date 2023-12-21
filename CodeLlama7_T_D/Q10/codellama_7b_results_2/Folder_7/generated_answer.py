
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer in the list
    for i in range(323, len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd_index = i
            break

    else:

        # If no odd integers exist in the specified range, return an empty list

        return []

    # Find the index of the last odd integer in the list

    for i in range(first_odd_index, len(my_list)):
        if my_list[i] % 2 != 0:
            last_odd_index = i
            break

    else:

        # If no odd integers exist in the specified range, return an empty list

        return []

    # Return the list of all odd integers from index 323 to index 972, both exclusive

    return my_list[first_odd_index:last_odd_index]
