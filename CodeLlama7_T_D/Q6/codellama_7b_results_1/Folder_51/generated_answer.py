
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_negative_index = None
    for i in range(len(my_list)):
        if my_list[i] < 0:
            first_negative_index = i
            break

    # If no negative integers exist in the specified range, return an empty list
    if first_negative_index is None:
        return []

    # Find the last negative integer in the list

    last_negative_index = None
    for i in range(first_negative_index, len(my_list)):
        if my_list[i] < 0:
            last_negative_index = i

    # Return the list of all negative integers from index 6 to index 9, both exclusive

    return my_list[first_negative_index + 1:last_negative_index]
