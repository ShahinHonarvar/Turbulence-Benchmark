
def all_even_ints_inclusive(my_list):
    # Find the first even integer in the list
    for i in range(22, len(my_list)):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    else:

        return []

    # Find the last even integer in the list

    for i in range(start_index, len(my_list)):

        if my_list[i] % 2 == 0:

            end_index = i

            break


    else:


        return []


    # Create a new list of even integers from the specified range

    return [my_list[i] for i in range(start_index, end_index + 1) if my_list[i] % 2 == 0]
