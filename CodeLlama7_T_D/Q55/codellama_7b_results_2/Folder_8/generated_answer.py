
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current sublist
        product = 1

        # Add the current element to the current sublist
        sublist.append(circular_list[i])

        # Calculate the product of the current sublist
        for j in range(len(sublist)):
            product *= sublist[j]

        # If the product equals -41, add the current sublist to the list of sublists to return
        if product == -41:
            sublists.append(sublist)

    # Return the list of sublists found that have a product equal to -41
    return sublists
