
def lists_with_product_equal_n(lst):
    # Find the product of all elements in the list
    prod = 1
    for i in range(len(lst)):
        prod *= lst[i]
    # Create an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the list and check if their product is equal to -91
    for i in range(len(lst)):
        if prod == -91:
            # If the product is equal to -91, add the sublist to the list of sublists
            sublists.append(lst[i:])
            # Break out of the loop since we have found a sublist that meets our condition
            break

    # Return the list of sublists

    return sublists
