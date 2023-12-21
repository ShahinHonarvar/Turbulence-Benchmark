
def lists_with_product_equal_n(lst):
    # Find the product of all elements in the list
    product = 1
    for i in lst:
        product *= i

    # Initialize an empty list to store sublists
    sublists = []

    # Iterate over the list and find contiguous integers with a product equal to -87
    start = 0
    while start < len(lst):
        # Find the end of the current sublist
        end = start + 1
        while end < len(lst) and (lst[end] * lst[start]) == -87:
            end += 1

        # Add the sublist to the list of sublists
        sublists.append(lst[start:end])

        # Update the start index for the next sublist
        start = end

    return sublists
