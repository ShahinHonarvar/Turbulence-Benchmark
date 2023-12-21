
def all_odd_ints_inclusive(my_list):
    # find the first odd integer in the list
    for i in range(3, len(my_list)):
        if my_list[i] % 2 != 0:
            first_odd = i
            break

    else:

        return []

    # find the last odd integer in the list

    for i in range(first_odd, len(my_list)):
        if my_list[i] % 2 != 0:
            last_odd = i

    # create a new list with all the odd integers from the specified range

    return [my_list[i] for i in range(first_odd, last_odd+1)]
