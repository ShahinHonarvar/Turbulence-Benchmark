
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer in the list
    for i, x in enumerate(my_list):
        if x % 2 != 0:
            break

    # Find the index of the last odd integer in the list

    for j, y in enumerate(my_list[::-1]):
        if y % 2 != 0:
            break

    # Return the list of all odd integers from index 20 to index 51, both exclusive

    return my_list[i + 19:j - 13]
