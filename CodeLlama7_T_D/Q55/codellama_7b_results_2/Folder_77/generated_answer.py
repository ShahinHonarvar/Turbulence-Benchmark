
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the contiguous integers
        product = 1

        # Iterate over the remaining elements in the circular list
        for j in range(i + 1, len(circular_list) + i + 1):

            # Calculate the product of the contiguous integers
            product *= circular_list[j % len(circular_list)]

            # Check if the product is equal to 632
            if product == 632:

                # Add the sublist to the list of sublists
                sublists.append(circular_list[i:j])

    # Return the list of sublists
    return sublists
