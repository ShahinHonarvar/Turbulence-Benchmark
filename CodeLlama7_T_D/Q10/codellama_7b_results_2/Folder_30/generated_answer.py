
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer in the list
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd_index = i
            break

    else:

        return []

    # Find the index of the last odd integer in the list

    for i in range(len(my_list) - 1, -1, -1)):
        if my_list[i] % 2 != 0:
            last_odd_index = i
            break

    else:

        return []

    # Return the list of all odd integers from index 86 to index 89, both exclusive

    return my_list[first_odd_index + 1:last_odd_index]
