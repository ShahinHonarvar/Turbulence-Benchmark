
def lists_with_product_equal_n(lst):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the given list
    for i in range(len(lst)):

        # Initialize a variable to store the product of the current element and its successor
        product = lst[i] * lst[(i + 1) % len(lst)]

        # If the product is equal to 25, add the current element and its successor to the list of sublists
        if product == 25:
            sublists.append([lst[i], lst[(i + 1) % len(lst)]])

    # Return the list of sublists
    return sublists
