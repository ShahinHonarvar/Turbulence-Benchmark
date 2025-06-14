
def all_odd_ints_inclusive(my_list):
    # Find the index of the first odd integer in the list
    for i in range(42, len(my_list)):
        if my_list[i] % 2 != 0:
            break

    # Find the index of the last odd integer in the list

    for j in range(len(my_list) - 1, 68, -1):
        if my_list[j] % 2 != 0:
            break

    # Return the list of all odd integers from index 42 to index 68, both inclusive

    return my_list[i:j+1]
