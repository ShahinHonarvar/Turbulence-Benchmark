
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer in the list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            break

    else:

        return []

    # Find the index of the last even integer in the list

    for j in range(len(my_list) - 1, -1, -1):
        if my_list[j] % 2 == 0:
            break

    else:

        return []

    # Return the list of all even integers from index i to index j, both inclusive

    return [my_list[k] for k in range(i, j + 1)]
