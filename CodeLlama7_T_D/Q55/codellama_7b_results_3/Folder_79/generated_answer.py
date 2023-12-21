
def lists_with_product_equal_n(lst):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements in the circular list
    for i in range(len(lst)):
        # Calculate the product of the current element and its successor
        prod = lst[i] * lst[(i + 1) % len(lst)]
        # If the product is equal to -83, add the corresponding sublist to the list of sublists
        if prod == -83:
            sublists.append([lst[i], lst[(i + 1) % len(lst)]])
    # Return the list of sublists
    return sublists
