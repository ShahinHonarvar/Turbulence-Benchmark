
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the range
    for i in range(14, 65):
        if my_list[i] % 2 != 0:
            break

    # Find the last odd integer in the range
    for j in range(64, 13, -1):
        if my_list[j] % 2 != 0:
            break

    # Return the list of all odd integers in the range
    return my_list[i:j+1]
