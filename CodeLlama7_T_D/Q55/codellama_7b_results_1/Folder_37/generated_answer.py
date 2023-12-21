
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Iterate over the elements of the given list from the current index to the end of the list
        for j in range(i, len(my_list)):
            # Multiply the current element by the previous product
            product *= my_list[j]

            # If the product equals -76, add the sublist to the returned list and break out of the inner loop
            if product == -76:
                sublists.append(my_list[i:j+1])
                break

    # Return the list of sublists
    return sublists
