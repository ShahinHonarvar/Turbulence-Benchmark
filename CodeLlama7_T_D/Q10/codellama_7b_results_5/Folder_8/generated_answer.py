
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer in the list
    for i in range(56, len(my_list)):
        if my_list[i] % 2 != 0:
            break

    # Find the index of the last odd integer in the list

    for j in range(92, -1, -1):
        if my_list[j] % 2 != 0:
            break

    # Return the list of all odd integers from index 56 to index 92, both exclusive

    return my_list[i + 1 : j]
