
def all_even_ints_exclusive(my_list):
    # Find the first even integer index
    for i in range(385, len(my_list), 1):
        if my_list[i] % 2 == 0:
            break

    # Find the last even integer index
    for j in range(len(my_list) - 1, 385, -1):
        if my_list[j] % 2 == 0:
            break

    # Return the list of all even integers from the specified range
    return [my_list[i] for i in range(385, j + 1, 1)]
