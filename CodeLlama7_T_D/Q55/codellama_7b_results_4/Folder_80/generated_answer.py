
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Add the current element to the current sublist
        sublist.append(circular_list[i])

        # Calculate the product of all the elements in the current sublist
        for j in range(len(sublist)):
            product *= sublist[j]

        # If the product equals 43, add the sublist to the list of sublists
        if product == 43:
            sublists.append(sublist)

    # Return the list of sublists
    return sublists
