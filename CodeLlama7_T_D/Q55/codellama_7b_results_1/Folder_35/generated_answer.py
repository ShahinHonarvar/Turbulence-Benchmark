
def lists_with_product_equal_n(lst, n):
    # Create an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(lst)):
        # Initialize a variable to store the product of the current element and its predecessor
        prod = 1

        # Iterate through the elements of the circular list starting from the current element
        for j in range(i, len(lst)):
            # Multiply the current element and its predecessor
            prod *= lst[j]

            # If the product equals n, add the sublist to the empty list
            if prod == n:
                sublists.append(lst[i:j+1])

    # Return the empty list if no such sublist exists
    return sublists or []
