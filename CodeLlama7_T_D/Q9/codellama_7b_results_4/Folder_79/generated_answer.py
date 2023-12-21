
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the list
    for i in range(4, len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd = i
            break

    else:

        return []

    # Find the last odd integer in the list

    for i in range(first_odd, len(my_list)):
        if my_list[i] % 2 != 0:
            last_odd = i

    # Return the list of all odd integers in the specified range

    return my_list[first_odd:last_odd+1]
