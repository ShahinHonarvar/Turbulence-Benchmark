
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Loop through each element in the current sublist
        for j in range(i, len(circular_list)):
            # Multiply the current element by the product of all previous elements
            product *= circular_list[j]

            # If the product equals 29, add the current sublist to the list of sublists
            if product == 29:
                sublists.append(circular_list[i:j+1])

    # Return the list of sublists that have a product equal to 29
    return sublists
