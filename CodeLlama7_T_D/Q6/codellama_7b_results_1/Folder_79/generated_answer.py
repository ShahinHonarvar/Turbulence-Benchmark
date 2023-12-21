
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    for i in range(3, len(my_list)):
        if my_list[i] < 0:
            first_negative = i
            break

    # If no negative integers exist in the specified range, return an empty list
    if first_negative == None:
        return []

    # Find the last negative integer in the list

    for j in range(first_negative, len(my_list)):
        if my_list[j] < 0:
            last_negative = j

    # Return a list of all negative integers from index 3 to index 8, both exclusive

    return my_list[first_negative + 1:last_negative]
