
def all_pos_ints_inclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((i for i in my_list if i > 0), None)
    # If no positive integers exist in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last positive integer in the list

    last_pos_int = next((i for i in reversed(my_list) if i > 0), None)

    # Create a list of all positive integers from index 56 to index 82, both inclusive

    pos_ints = []

    for i in range(56, 83):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    return pos_ints
