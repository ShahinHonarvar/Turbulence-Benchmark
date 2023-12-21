
def all_even_ints_inclusive(my_list):
    # Find the first even integer in the range
    for i in range(62, 78 + 1):
        if my_list[i] % 2 == 0:
            start = i
            break

    else:

        return []


    # Find the last even integer in the range

    for i in range(start, -1, -1):
        if my_list[i] % 2 == 0:
            end = i
            break

    else:

        return []


    # Return a list of all even integers in the range

    return [my_list[i] for i in range(start, end + 1)]
