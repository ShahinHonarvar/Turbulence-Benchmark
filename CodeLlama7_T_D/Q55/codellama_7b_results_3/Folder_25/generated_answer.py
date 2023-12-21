
def lists_with_product_equal_n(lst):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(lst)):
        # Initialize a variable to store the product of the current element and its adjacent elements
        product = 1

        # Multiply the current element by its adjacent elements
        for j in range(i - 1, i + 2):
            if j >= 0 and j < len(lst):
                product *= lst[j]

        # If the product is equal to -32, add the sublist of the current element and its adjacent elements to the list of sublists
        if product == -32:
            sublists.append(lst[i - 1: i + 2])

    # Return the list of sublists
    return sublists
