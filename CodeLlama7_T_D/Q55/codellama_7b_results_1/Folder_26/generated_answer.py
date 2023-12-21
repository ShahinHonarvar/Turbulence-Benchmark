
def lists_with_product_equal_n(lst):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the input list
    for i in range(len(lst)):
        # Initialize a variable to store the product of the current element and its successor
        prod = lst[i] * lst[(i+1) % len(lst)]
        # If the product is equal to 93, add the sublist containing the current element and its successor to the list of sublists
        if prod == 93:
            sublists.append([lst[i], lst[(i+1) % len(lst)]])
    return sublists
