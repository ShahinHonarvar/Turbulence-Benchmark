
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the current product
        current_product = 1

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list) + 1):
            # Multiply the current element by the previous product
            current_product *= circular_list[j - 1]

            # If the product is equal to -36, add the sublist to the list of sublists
            if current_product == -36:
                sublists.append(circular_list[i:j])

    # Return the list of sublists
    return sublists
