
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Calculate the product of the elements in the current sublist
        for j in range(i, len(my_list)):
            product *= my_list[j]

        # If the product equals -30, add the current sublist to the list of sublists
        if product == -30:
            sublists.append(my_list[i:j+1])

    # Return the list of sublists
    return sublists
