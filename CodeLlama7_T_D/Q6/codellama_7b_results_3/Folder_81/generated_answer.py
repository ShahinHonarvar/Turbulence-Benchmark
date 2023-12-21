
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_neg_int = next((x for x in my_list if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_neg_int is None:
        return []

    # Find the last negative integer in the list

    last_neg_int = next((x for x in my_list[10:] if x < 0), None)

    # Return the list of all negative integers from index 10 to index 100, both exclusive

    return my_list[10:last_neg_int + 1]
