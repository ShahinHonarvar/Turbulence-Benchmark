
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its successor
        product = circular_list[i] * circular_list[(i + 1) % len(circular_list)]

        # If the product is equal to -81, add the current element and its successor to the list of sublists
        if product == -81:
            sublists.append([circular_list[i], circular_list[(i + 1) % len(circular_list)]]))

    # Return the list of sublists
    return sublists
