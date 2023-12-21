
def lists_with_product_equal_n(lst, n):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(lst)):
        # Initialize a variable to store the product of the current element and its previous neighbors
        prod = 1

        # Iterate over the previous neighbors of the current element
        for j in range(i - 1, -1, -1):
            # Calculate the product of the current element and its previous neighbor
            prod *= lst[j]

            # If the product is equal to the target value 'n', add the sublist containing the previous neighbors to the list of sublists
            if prod == n:
                sublists.append(lst[j:i + 1])

    # Return the list of sublists, or an empty list if no such sublists exist
    return sublists or []
