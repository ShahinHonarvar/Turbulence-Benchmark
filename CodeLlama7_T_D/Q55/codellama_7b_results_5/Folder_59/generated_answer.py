
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Get the current element and its predecessor and successor
        curr_element = circular_list[i]
        pred_element = circular_list[(i - 1) % len(circular_list)]
        succ_element = circular_list[(i + 1) % len(circular_list)]

        # Check if the current element is part of a sublist with product equal to -3
        if curr_element * pred_element * succ_element == -3:

            # Add the sublist to the list of sublists
            sublists.append([curr_element, pred_element, succ_element])

    # Return the list of sublists
    return sublists
