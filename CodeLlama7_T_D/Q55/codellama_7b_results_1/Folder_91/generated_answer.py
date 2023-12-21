
def lists_with_product_equal_n(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) <= 1:
        return []

    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the list
    for i in range(len(my_list)):

        # Check if the product of the elements from the current element to the end of the list is equal to 2
        if my_list[i] * my_list[(i + 1) % len(my_list)] == 2:

            # Add the sublist containing the contiguous integers from the given list such that their product equals 2
            sublists.append(my_list[i:(i + 1) % len(my_list)]))

    return sublists
