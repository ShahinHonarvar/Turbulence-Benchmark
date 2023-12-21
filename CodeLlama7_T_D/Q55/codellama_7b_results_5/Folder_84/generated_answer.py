
def lists_with_product_equal_n(lst):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(lst)):

        # Compute the product of the elements from the current element up to the end of the list
        prod_up = 1
        for j in range(i, len(lst)):
            prod_up *= lst[j]

        # Compute the product of the elements from the beginning of the list up to the current element
        prod_down = 1
        for j in range(len(lst) - 1, -1, -1):
            if j >= i:
                break

            prod_down *= lst[j]

        # If the product of the elements from the current element up to the end of the list equals -906, add the sublist to the returned list
        if prod_up == -906:
            sublists.append(lst[i:])

        # If the product of the elements from the beginning of the list up to the current element equals -906, add the sublist to the returned list
        if prod_down == -906:
            sublists.append(lst[:i + 1])

    # Return the list of sublists that satisfy the condition
    return sublists
