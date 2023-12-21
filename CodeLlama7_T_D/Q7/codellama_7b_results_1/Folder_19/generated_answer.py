
def all_even_ints_inclusive(my_list):
    # find the first even integer in the list
    for i in range(3, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i
            break

    else:

        return []

    # find the last even integer in the list

    for i in range(start, -1, -1):
        if my_list[i] % 2 == 0:
            end = i
            break

    else:

        return []

    # create a new list with all even integers from start to end

    return [my_list[i] for i in range(start, end + 1) if my_list[i] % 2 == 0]
