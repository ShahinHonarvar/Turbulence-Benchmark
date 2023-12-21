
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers that have a product equal to -51
    for i in range(len(circular_list)):
        # Initialize a variable to store the current product
        current_product = 1

        # Iterate over the remaining elements of the circular list starting from the current element
        for j in range(i+1, len(circular_list)+1):
            # Multiply the current product by the next element of the circular list
            current_product *= circular_list[j-1]

            # If the current product is equal to -51, append the sublist containing the contiguous integers to the sublists list and reset the current product to 1
            if current_product == -51:
                sublists.append(circular_list[i:j])
                current_product = 1

    # Return the list of sublists that have a product equal to -51, or an empty list if no such sublist exists
    return sublists
