
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Iterate over the elements of the given list starting from the current index
        for j in range(i, len(my_list)):
            # Multiply the current element by the product variable
            product *= my_list[j]

            # If the product variable is equal to 36, add the sublist to the list of sublists and break out of the inner loop
            if product == 36:
                sublists.append(my_list[i:j+1])
                break

    # Return the list of sublists
    return sublists
