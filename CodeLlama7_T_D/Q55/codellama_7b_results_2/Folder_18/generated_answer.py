
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Calculate the product of the elements from the current index to the end of the list
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

        # If the product is equal to 36, add the sublist to the list of sublists
        if product == 36:
            sublists.append(circular_list[i:])

    # Return the list of sublists
    return sublists
