
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(78, len(my_list)):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    # Find the last even integer in the list

    for i in range(start_index, len(my_list)):
        if my_list[i] % 2 == 0:
            end_index = i

    # Return the list of all even integers from start_index to end_index exclusive

    return my_list[start_index:end_index]
