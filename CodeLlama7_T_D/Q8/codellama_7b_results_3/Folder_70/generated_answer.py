
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(38, len(my_list), 1):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    else:

        return []

    # Find the last even integer in the list

    for i in range(start_index, len(my_list), -1):
        if my_list[i] % 2 == 0:
            end_index = i
            break

    else:

        return []

    # Return the list of even integers from the specified range

    return my_list[start_index + 1:end_index]
