
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with a product equal to -65
    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current sublist and its product
        current_sublist = []
        current_product = 1

        # Iterate over the circular list from the current index to the end of the list
        for j in range(i, len(circular_list)):
            # Add the current element to the sublist and update the product
            current_sublist.append(circular_list[j])
            current_product *= circular_list[j]

            # If the product is equal to -65, add the sublist to the list of sublists and reset the variables
            if current_product == -65:
                sublists.append(current_sublist)
                current_sublist = []
                current_product = 1

    # Return the list of sublists
    return sublists
