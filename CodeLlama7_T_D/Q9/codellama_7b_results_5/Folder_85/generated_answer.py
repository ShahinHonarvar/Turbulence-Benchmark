
def all_odd_ints_inclusive(my_list):
    # Find the index of the first odd integer
    for i in range(6, len(my_list)):
        if my_list[i] % 2 != 0:
            break

    # Find the index of the last odd integer

    for j in range(len(my_list)-1, 6, -1):
        if my_list[j] % 2 != 0:
            break

    # Create a new list with all odd integers from the specified range

    return [my_list[k] for k in range(i, j+1)]
