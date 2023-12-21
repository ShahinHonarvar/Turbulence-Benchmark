
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    first_neg_int = next((i for i in my_list if i < 0), None)
    # If there are no negative integers in the list, return an empty list
    if first_neg_int is None:
        return []

    # Find the last negative integer in the list

    last_neg_int = next((i for i in my_list[::-1] if i < 0), None)

    # Return the list of all negative integers from index 70 to index 200, both exclusive

    return [i for i in my_list[70:200] if i < 0]
