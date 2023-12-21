
def all_odd_ints_inclusive(my_list):
    # Find the index of the first odd integer in the list
    for i, num in enumerate(my_list):
        if num % 2 != 0:
            break

    # Find the index of the last odd integer in the list

    for j, num in enumerate(reversed(my_list)):
        if num % 2 != 0:
            break

    # Return the list of all odd integers from the specified range

    return my_list[i:j+1]
