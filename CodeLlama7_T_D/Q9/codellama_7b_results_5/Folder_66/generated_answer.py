
def all_odd_ints_inclusive(my_list):
    # Find the index of the first odd integer in the list
    for i, x in enumerate(my_list):
        if x % 2 != 0:
            break

    else:

        return []

    # Find the index of the last odd integer in the list

    for i in range(len(my_list) - 1, -1, -1)):
        if my_list[i] % 2 != 0:
            break

    else:

        return []

    # Return the list of all odd integers from index 50 to index 54, both inclusive

    return [my_list[i] for i in range(50, 55) if my_list[i] % 2 != 0]]
