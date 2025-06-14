
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and compute the product of each contiguous sequence of integers
    for i in range(len(circular_list))):
        product = 1

        # Compute the product of the current sequence of integers
        for j in range(i, len(circular_list))):
            product *= circular_list[j]

        # If the product is equal to 990, add the corresponding sublist to the returned list
        if product == 990:
            sublists.append(circular_list[i:j+1])

    # Return the list of sublists found
    return sublists
