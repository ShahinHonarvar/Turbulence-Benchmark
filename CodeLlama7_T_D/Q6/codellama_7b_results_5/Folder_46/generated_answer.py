
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((i for i in my_list if i < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_negative is None:
        return []

    # Find the last negative integer in the list

    last_negative = next((i for i in my_list[20:] if i < 0), None)

    # Return the list of all negative integers from index 20 to index 43, both exclusive

    return my_list[first_negative + 1:last_negative - 1]
