
def all_even_ints_exclusive(my_list):
    # Find the first even integer index
    for i in range(57, len(my_list)):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    # Find the last even integer index

    for i in range(start_index, len(my_list)):
        if my_list[i] % 2 == 0:
            end_index = i
            break

    # Return the list of all even integers from the specified range

    return my_list[start_index:end_index+1]
