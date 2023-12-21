
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its neighbors
        curr_element = circular_list[i]
        prev_element = circular_list[(i - 1) % len(circular_list)]
        next_element = circular_list[(i + 1) % len(circular_list)]
        # Check if the product of the current element and its neighbors is equal to -5
        if curr_element * prev_element * next_element == -5:
            # If so, add the sublist to the list of sublists
            sublists.append([curr_element, prev_element, next_element])
    # Return the list of sublists
    return sublists
