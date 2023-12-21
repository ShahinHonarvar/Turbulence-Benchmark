
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    for i in range(70, len(my_list)):
        if my_list[i] < 0:
            first_negative = i
            break

    else:

        # If no negative integers exist in the specified range, return an empty list.
        return []

    # Find the last negative integer in the list

    for i in range(first_negative, len(my_list)):
        if my_list[i] < 0:
            last_negative = i

    # Return the list of all negative integers from index 70 to index 98, both exclusive.
    return my_list[first_negative:last_negative]
