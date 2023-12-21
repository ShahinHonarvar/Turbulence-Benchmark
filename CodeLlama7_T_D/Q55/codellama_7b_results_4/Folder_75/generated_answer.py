
def lists_with_product_equal_n(circular_list, n):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find all contiguous sublists whose product is equal to n
    for i in range(len(circular_list)):
        # Initialize a variable to store the current product
        product = 1

        # Iterate over the elements of the current sublist, starting from the head
        for j in range(i, len(circular_list)):
            # Update the product with the current element
            product *= circular_list[j]

            # If the product is equal to n, add the current sublist to the list of sublists and break out of the inner loop
            if product == n:
                sublists.append(circular_list[i:j + 1])
                break

        # If no sublist with a product equal to n is found, return an empty list
        if not sublists:
            return []

    # Return the list of sublists with their product equal to n
    return sublists
