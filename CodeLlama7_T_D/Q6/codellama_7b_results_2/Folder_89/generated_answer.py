
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_negative is None:
        return []

    # Find the last negative integer in the list

    last_negative = next((i for i, x in enumerate(my_list[first_negative:]) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if last_negative is None:
        return []

    # Return the list of all negative integers from index 51 to index 76, both exclusive
    return my_list[first_negative + 50:last_negative + 50]
