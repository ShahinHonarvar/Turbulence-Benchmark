
def lists_with_product_equal_n(lst):
    # Initialize variables to keep track of sublists and products
    sublists = []
    product = 1

    # Iterate over the elements of the list
    for i in range(len(lst)):

        # If the product is equal to -837, add the sublist to the list of sublists
        if product == -837:
            sublists.append(lst[i-product:i])

        # Multiply the current element by the product
        product *= lst[i]

    # Return the list of sublists
    return sublists
