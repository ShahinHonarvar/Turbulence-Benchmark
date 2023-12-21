
def lists_with_product_equal_n(lst):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(lst)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Iterate over the remaining elements of the given list after the current element
        for j in range(i + 1, len(lst)):
            # Multiply the current product by the current element and store the result back in the variable
            product *= lst[j]

            # If the product equals n, add the sublist to the list of sublists and break out of the inner loop
            if product == n:
                sublists.append(lst[i:j + 1])
                break

    # Return the list of sublists
    return sublists
