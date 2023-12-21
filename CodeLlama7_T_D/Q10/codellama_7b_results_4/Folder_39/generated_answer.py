
def all_odd_ints_exclusive(my_list):
    # find index of first odd integer
    for i in range(43, len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd_index = i
            break

    # find index of last odd integer

    for i in range(first_odd_index, len(my_list)):
        if my_list[i] % 2 != 0:
            last_odd_index = i

    # return list of all odd integers from first to last

    return my_list[first_odd_index:last_odd_index+1]
