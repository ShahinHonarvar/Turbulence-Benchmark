
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(42, len(my_list)):
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


    # Create a new list of even integers

    return my_list[start_index:end_index+1]
