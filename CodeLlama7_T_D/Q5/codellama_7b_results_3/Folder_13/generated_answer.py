
def all_neg_ints_inclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If there are no negative integers in the list, return an empty list
    if first_negative is None:
        return []

    # Find the last negative integer in the list

    last_negative = next((i for i, x in enumerate(my_list[first_negative:]) if x < 0), None)

    # Return the list of all negative integers from index 25 to index 87, both inclusive

    return my_list[first_negative:last_negative+1]
