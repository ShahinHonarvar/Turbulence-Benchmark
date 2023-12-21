
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with a product equal to -23
    for i in range(len(circular_list)) :
        # Initialize a variable to store the product of the current and subsequent elements
        prod = 1

        # Calculate the product of the current and subsequent elements
        for j in range(i, len(circular_list)) :
            prod *= circular_list[j]

            # If the product is equal to -23, add the sublist to the list of sublists
            if prod == -23 :
                sublists.append(circular_list[i:j+1])

    # Return the list of sublists

    return sublists
