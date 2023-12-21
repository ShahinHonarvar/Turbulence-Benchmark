
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Iterate over the remaining elements of the given list
        for j in range(i + 1, len(my_list) + 1):
            # Calculate the product of the elements in the current sublist
            product *= my_list[j - 1]

            # Check if the product is equal to -83
            if product == -83:
                # Append the current sublist to the list of sublists
                sublists.append(my_list[i:j])

    # Return the list of sublists
    return sublists
