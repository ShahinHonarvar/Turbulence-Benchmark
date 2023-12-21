
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with product equal to -91
    for i in range(len(circular_list)):
        current_product = 1

        # Check if the current element has a product equal to -91
        if current_product == -91:
            # Add the contiguous sublist to the list of sublists
            sublists.append(circular_list[i:])

    # Return the list of sublists
    return sublists
