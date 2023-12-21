
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Calculate the product of the elements in the current sublist
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

        # Check if the product is equal to -82
        if product == -82:
            # Add the current sublist to the list of sublists
            sublists.append(circular_list[i:])

    # Return the list of sublists
    return sublists
