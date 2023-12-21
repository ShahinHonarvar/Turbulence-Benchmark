
def all_odd_ints_inclusive(my_list):
    # find the index of the first odd integer
    for i in range(75, len(my_list)):
        if my_list[i] % 2 != 0:
            first_index = i
            break

    # find the index of the last odd integer

    for i in range(first_index, len(my_list)):
        if my_list[i] % 2 != 0:
            last_index = i

    # return the list of all odd integers from the specified range

    return my_list[first_index:last_index+1]
