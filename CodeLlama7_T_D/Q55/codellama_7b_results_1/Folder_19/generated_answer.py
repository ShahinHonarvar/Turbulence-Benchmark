
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its previous element (if any)
        product = 1

        # Iterate over the remaining elements of the circular list starting from the current element
        for j in range(i + 1, len(circular_list)):
            # Update the product by multiplying the current element by its previous element (if any)
            product *= circular_list[j]

        # If the product is equal to -54, add the sublist containing the contiguous integers from the given list such that their product equals -54
        if product == -54:
            sublists.append(circular_list[i:] + circular_list[:i])

    # Return the list of sublists containing the contiguous integers from the given list such that their product equals -54
    return sublists
