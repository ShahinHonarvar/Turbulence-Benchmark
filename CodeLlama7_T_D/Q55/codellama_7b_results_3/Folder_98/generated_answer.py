
def lists_with_product_equal_n(lst):
    # initialize an empty list for the result
    result = []

    # loop over the elements of the given list
    for i in range(len(lst)):
        # compute the product of the current element and all previous elements
        prod = 1
        for j in range(i):
            prod *= lst[j]

        # add the current sublist to the result if its product equals -1
        if prod == -1:
            result.append(lst[i-len(result):i])

    # return the list of sublists with their product equal to -1
    return result
