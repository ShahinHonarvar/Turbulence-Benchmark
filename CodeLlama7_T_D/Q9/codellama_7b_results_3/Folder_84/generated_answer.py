
def all_odd_ints_inclusive(my_list):
    # find the index of the first odd integer
    for i in range(43, len(my_list)):
        if my_list[i] % 2 != 0:
            break

    # find the index of the last odd integer
    for j in range(len(my_list)-1, -1, -1):
        if my_list[j] % 2 != 0:
            break

    # return the list of all odd integers from the specified range
    return [my_list[i] for i in range(43, j+1)]
