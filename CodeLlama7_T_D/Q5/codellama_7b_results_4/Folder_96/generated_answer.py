
def all_neg_ints_inclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_negative is None:
        return []

    # Find the last negative integer in the list

    last_negative = next((i for i, x in enumerate(my_list[first_negative:]) if x < 0), None)
    # Return a list of all negative integers from index 50 to index 200, both inclusive
    return my_list[first_negative:last_negative+1]
