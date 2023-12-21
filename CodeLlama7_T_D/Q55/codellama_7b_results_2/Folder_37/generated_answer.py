
def lists_with_product_equal_n(circlist):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given circular list
    for i in range(len(circlist)):
        # Get the current element and its successor
        current = circlist[i]
        next = circlist[(i+1)%len(circlist)]

        # Check if the product of the current element and its successor is equal to -76
        if current * next == -76:
            # If it is, add the sublist containing the current and successor elements to the list of sublists
            sublists.append([current, next])

    # Return the list of sublists
    return sublists
