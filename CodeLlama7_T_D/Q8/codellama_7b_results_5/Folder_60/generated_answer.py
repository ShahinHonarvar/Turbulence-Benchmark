
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(44, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i
            break

    else:

        return []

    # Find the last even integer in the list

    for i in range(start, len(my_list)):
        if my_list[i] % 2 == 0:
            end = i
            break

    else:

        return []

    # Return a new list with all even integers from the specified range

    return [my_list[i] for i in range(start, end + 1) if my_list[i] % 2 == 0]
