
def lists_with_product_equal_n(lst, n):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the given list
    for i in range(len(lst)):
        # Compute the product of the elements from the current element to the end of the list
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[j]
            # If the product is equal to n, add the sublist to the result list and continue with the next element
            if prod == n:
                sublists.append(lst[i:j+1])
                i = j + 1
                break

    return sublists
