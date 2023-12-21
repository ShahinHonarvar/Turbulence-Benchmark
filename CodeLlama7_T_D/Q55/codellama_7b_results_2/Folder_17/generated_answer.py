
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find all contiguous sublists with a product equal to 18
    for i in range(len(circular_list))):
        # Initialize variables to keep track of the current sublist and its product
        current_sublist = []
        current_product = 1

        # Iterate over the remaining elements in the circular list
        for j in range(i, len(circular_list))):
            # Add the current element to the current sublist
            current_sublist.append(circular_list[j])

            # Update the product of the current sublist
            current_product *= circular_list[j]

            # If the product of the current sublist is equal to 18, add it to the list of sublists and reset the variables
            if current_product == 18:
                sublists.append(current_sublist)
                current_sublist = []
                current_product = 1

    # Return the list of sublists with a product equal to 18
    return sublists
