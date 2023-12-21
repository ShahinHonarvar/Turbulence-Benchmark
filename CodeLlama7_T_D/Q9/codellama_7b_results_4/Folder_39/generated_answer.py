
def all_odd_ints_inclusive(my_list):
    # Find the index of the first odd integer
    first_odd_index = None
    for i in range(20, len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd_index = i
            break

    # Find the index of the last odd integer

    last_odd_index = None
    for i in range(len(my_list) - 1, 20, -1):
        if my_list[i] % 2 != 0:
            last_odd_index = i
            break

    # Return the list of all odd integers from index 20 to index 30, both inclusive

    if first_odd_index is not None and last_odd_index is not None:
        return my_list[first_odd_index : last_odd_index + 1]

    else:

        return []
