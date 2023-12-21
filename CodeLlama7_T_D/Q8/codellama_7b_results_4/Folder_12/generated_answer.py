
def all_even_ints_exclusive(my_list):
    # Find the index of the first even integer
    for i in range(23, len(my_list)):
        if my_list[i] % 2 == 0:
            start_index = i + 1
            break

    else:

        return []


    # Find the index of the last even integer

    for i in range(start_index, len(my_list)):
        if my_list[i] % 2 == 0:
            end_index = i - 1
            break

    else:

        return []


    # Return the list of all even integers from index 23 to index 45, both exclusive

    return my_list[start_index:end_index]
