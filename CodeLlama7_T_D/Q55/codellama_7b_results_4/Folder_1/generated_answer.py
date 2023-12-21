
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Add the current element to the product
        product *= circular_list[i]

        # If the product equals -51, add the current sublist to the list of sublists
        if product == -51:
            sublists.append(circular_list[i:])

    # Return the list of sublists
    return sublists
