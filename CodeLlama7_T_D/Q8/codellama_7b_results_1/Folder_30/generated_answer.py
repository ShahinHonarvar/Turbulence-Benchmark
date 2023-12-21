
def all_even_ints_exclusive(my_list):
    # Find the index of the first even integer in the list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    else:

        return []


    # Find the index of the last even integer in the list

    for i in range(len(my_list) - 1, -1, -1):

        if my_list[i] % 2 == 0:

            end_index = i

            break


    else:


        return []


    # Return the list of all even integers in the specified range

    return my_list[start_index:end_index + 1]
