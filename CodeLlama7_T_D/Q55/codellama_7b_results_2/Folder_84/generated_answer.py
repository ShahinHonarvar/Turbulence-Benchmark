
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and calculate the product of contiguous integers
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]

        # If the product is equal to -906, add the sublist to the returned list
        if product == -906:
            sublists.append(circular_list[i:])

    # Return the list of sublists that have a product equal to -906
    return sublists
