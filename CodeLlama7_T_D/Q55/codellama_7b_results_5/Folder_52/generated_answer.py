
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []
    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Get the current element and its neighbors
        curr_elem = circular_list[i]
        prev_elem = circular_list[(i - 1) % len(circular_list)]
        next_elem = circular_list[(i + 1) % len(circular_list)]
        # Calculate the product of the current element and its neighbors
        curr_prod = curr_elem * prev_elem * next_elem
        # Check if the product is equal to the given value
        if curr_prod == 37:
            # Add the sublist to the list of sublists
            sublists.append([curr_elem, prev_elem, next_elem])
    return sublists
