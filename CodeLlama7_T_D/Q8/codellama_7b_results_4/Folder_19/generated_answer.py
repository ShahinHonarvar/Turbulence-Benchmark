
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(2, len(my_list), 2):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    else:

        return []

    # Find the last even integer in the list

    for i in range(start_index, len(my_list), 2):
        if my_list[i] % 2 == 0:
            end_index = i

    # Return the list of all even integers from index 2 to index 5, both exclusive

    return my_list[start_index:end_index+1]
