
def all_neg_ints_inclusive(my_list):
    # Find the first negative integer in the list
    first_neg_int = next((x for x in my_list if x < 0), None)
    # If no negative integers exist in the list, return an empty list
    if first_neg_int is None:
        return []

    # Find the last negative integer in the list

    last_neg_int = next((x for x in my_list[::-1] if x < 0), None)
    # If no negative integers exist in the list, return an empty list
    if last_neg_int is None:
        return []

    # Return the list of all negative integers from index 37 to index 51, both inclusive

    return [x for x in my_list[37:52] if x < 0]
