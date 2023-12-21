
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_neg_int = next((x for x in my_list if x < 0), None)
    # If no negative integers exist in the list, return an empty list
    if first_neg_int is None:
        return []

    # Find the last negative integer in the list

    last_neg_int = next((x for x in my_list[::-1] if x < 0), None)

    # If no negative integers exist in the specified range, return an empty list

    if last_neg_int is None:
        return []

    # Return the list of all negative integers from index 15 to index 40, both exclusive

    return [x for x in my_list[15:40] if x < 0]
