
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the list
    for i in range(23, len(my_list)):
        if my_list[i] % 2 != 0:
            break

    # Find the last odd integer in the list

    for j in range(len(my_list) - 1, 23, -1):
        if my_list[j] % 2 != 0:
            break

    # Return the list of all odd integers from index 23 to index 45, both exclusive

    return my_list[i + 1: j]
