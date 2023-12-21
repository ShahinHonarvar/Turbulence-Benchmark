
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_negative = next((i for i in my_list if i < 0), None)
    # If no negative integers exist in the list, return an empty list
    if first_negative is None:
        return []

    # Get the index of the first negative integer
    first_negative_index = my_list.index(first_negative)

    # Find the last negative integer in the list
    last_negative = next((i for i in my_list[first_negative_index:] if i < 0), None)

    # If no negative integers exist in the specified range, return an empty list
    if last_negative is None:
        return []

    # Get the index of the last negative integer
    last_negative_index = my_list.index(last_negative) + first_negative_index

    # Return the list of all negative integers from index 18 to index 37, both exclusive
    return my_list[first_negative_index + 18:last_negative_index + 1]
