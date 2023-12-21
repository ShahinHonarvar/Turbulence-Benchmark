
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the range
    for i in range(43, len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd_index = i
            break

    # Find the last odd integer in the range

    for i in range(first_odd_index, len(my_list)):
        if my_list[i] % 2 != 0:
            last_odd_index = i
            break

    # Return the list of all odd integers in the range

    return my_list[first_odd_index:last_odd_index+1]
