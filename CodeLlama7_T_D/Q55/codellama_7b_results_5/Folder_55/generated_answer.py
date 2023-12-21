
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):
        # Calculate the product of the elements from the current element up to the end of the list
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

        # If the product is equal to -6, add the sublist to the list of sublists
        if product == -6:
            sublists.append(circular_list[i:])

    # Return the list of sublists
    return sublists
