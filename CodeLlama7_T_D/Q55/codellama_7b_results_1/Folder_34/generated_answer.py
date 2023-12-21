
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Set the current element as the starting element of the sublist
        current_element = circular_list[i]

        # Initialize a variable to store the product of the elements in the sublist
        product = 1

        # Loop through each element in the circular list that comes after the starting element
        for j in range(i + 1, len(circular_list)):
            # Multiply the current element by the next element in the list
            product *= circular_list[j]

            # If the product is equal to -81, add the sublist to the returned list and break out of the inner loop
            if product == -81:
                sublists.append(circular_list[i:j + 1])
                break

    # Return the list of sublists that have a product equal to -81
    return sublists
