
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to keep track of the current product
        current_product = 1

        # Loop through each element in the sublist
        for j in range(i, len(circular_list)):
            # Update the current product with the product of the current element and the next element
            current_product *= circular_list[j]

            # If the current product is equal to -46, add the sublist to the list of sublists
            if current_product == -46:
                sublists.append(circular_list[i:j+1])

    # Return the list of sublists
    return sublists
