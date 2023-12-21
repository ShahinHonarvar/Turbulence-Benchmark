
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and calculate the product of adjacent elements
    for i in range(len(circular_list)):# Calculate the product of the current element with the next element in the circular list
        product = circular_list[i] * circular_list[(i + 1) % len(circular_list)]

        # If the product is equal to -9, add it to the list of sublists
        if product == -9:
            sublists.append([circular_list[i], circular_list[(i + 1) % len(circular_list)]]))

    # Return the list of sublists
    return sublists
