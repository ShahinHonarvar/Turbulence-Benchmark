
def lists_with_product_equal_n(my_list):
    # Check if the list contains any duplicates
    if len(my_list) != len(set(my_list)):
        return []

    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):

        # Check if the product of the contiguous integers from the given list starting from the current element is equal to 91
        if my_list[i] * my_list[(i + 1) % len(my_list)] * my_list[(i + 2) % len(my_list)] == 91:
            # Add the sublist containing the contiguous integers from the given list starting from the current element to the returned list of sublists
            sublists.append([my_list[i], my_list[(i + 1) % len(my_list)], my_list[(i + 2) % len(my_list)]]])

    # Return the list of sublists containing the contiguous integers from the given list such that their product equals 91
    return sublists
