
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the list
    for i in range(len(my_list))
        if my_list[i] % 2 != 0:
            first_odd_index = i
            break

    # If no odd integers exist in the specified range, return an empty list
    if first_odd_index == None:
        return []

    # Find the last odd integer in the list

    for i in range(first_odd_index, len(my_list))):
        if my_list[i] % 2 != 0:
            last_odd_index = i
            break

    # Return the list of all odd integers from index 7 to index 9, both exclusive
    return my_list[first_odd_index : last_odd_index + 1]
