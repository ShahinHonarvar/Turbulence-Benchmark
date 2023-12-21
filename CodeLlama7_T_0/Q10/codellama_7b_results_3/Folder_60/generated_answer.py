
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the list
    for i in range(44, len(my_list)):
        if my_list[i] % 2 != 0:
            break

    # Find the last odd integer in the list

    for j in range(len(my_list) - 1, 91, -1):
        if my_list[j] % 2 != 0:
            break

    # Return the list of all odd integers in the specified range

    return my_list[i + 1:j]
