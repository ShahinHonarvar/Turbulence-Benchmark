
def all_neg_ints_inclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((x for x in my_list if x < 0), None)
    # If there are no negative integers, return an empty list
    if first_negative is None:
        return []

    # Find the last negative integer in the list
    last_negative = next(reversed(my_list), None)
    # If there are no negative integers, return an empty list
    if last_negative is None:
        return []

    # Return a new list of all negative integers between the first and last negative integers in the original list
    return [x for x in my_list if x >= first_negative and x <= last_negative]
