
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_negative is None or first_negative < 3:
        return []

    # Find the last negative integer in the list

    last_negative = next(i for i, x in enumerate(my_list) if x < 0, None)
    # If no negative integers exist in the specified range, return an empty list
    if last_negative is None or last_negative > 8:
        return []

    # Return the list of all negative integers from index 3 to index 8, both exclusive
    return my_list[first_negative + 1:last_negative]
