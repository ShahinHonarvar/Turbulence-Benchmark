
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its neighbors
        curr_element = circular_list[i]
        prev_element = circular_list[(i - 1) % len(circular_list)]
        next_element = circular_list[(i + 1) % len(circular_list)]

        # Check if the current element is a part of a sublist with product equal to 733
        if curr_element * prev_element * next_element == 733:
            # If it is, add it to the list of sublists
            sublists.append([curr_element, prev_element, next_element])

    # Return the list of sublists with product equal to 733
    return sublists
