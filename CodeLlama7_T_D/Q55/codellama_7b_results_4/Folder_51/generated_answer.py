
def lists_with_product_equal_n(lst):
    # Check if the input list is empty
    if len(lst) == 0:
        return []

    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the input list
    for i in range(len(lst)):

        # Check if the product of the elements in the current window is equal to -44
        prod = 1
        for j in range(i, min(i + len(lst), len(lst))):
            prod *= lst[j]
        if prod == -44:

            # Add the sublist to the list of sublists
            sublists.append(lst[i:min(i + len(lst), len(lst))]))

    return sublists
