
def all_neg_ints_exclusive(my_list):
    # Find the index of the first negative integer in the list
    first_negative = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If there are no negative integers in the list, return an empty list
    if first_negative is None:
        return []

    # Find the index of the last negative integer in the list

    last_negative = next((i for i, x in enumerate(my_list[first_negative:]) if x < 0), None)
    # If there are no negative integers in the specified range, return an empty list
    if last_negative is None:
        return []

    # Return the list of all negative integers from index 56 to index 92, both exclusive

    return my_list[first_negative + 1 : first_negative + last_negative + 1]
