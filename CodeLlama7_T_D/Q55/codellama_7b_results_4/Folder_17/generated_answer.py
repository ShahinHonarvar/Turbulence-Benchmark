
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Extract a contiguous sublist from the current element to the end of the list
        sublist = circular_list[i:]

        # Calculate the product of the elements in the sublist
        product = 1
        for j in range(len(sublist)):
            product *= sublist[j]

        # If the product equals n, append the sublist to the list of sublists
        if product == n:
            sublists.append(sublist)

    # Return the list of sublists
    return sublists
