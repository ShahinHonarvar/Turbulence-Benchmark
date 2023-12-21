
def lists_with_product_equal_n(lst, n):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the input list
    for i in range(len(lst)):

        # Initialize variables to keep track of the current sublist and its product
        sublist = [lst[i]]
        product = lst[i]

        # Check if the current element is equal to n
        if lst[i] == n:

            # If it is, add it to the list of sublists
            sublists.append(sublist)

    # Return the list of sublists
    return sublists
