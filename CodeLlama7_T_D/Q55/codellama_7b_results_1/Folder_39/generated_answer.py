
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Set the current element as the starting point of the sublist
        start = i

        # Initialize a product variable to store the product of elements in the sublist
        product = 1

        # Loop through each element in the circular list from the starting point to the end of the list
        for j in range(start, len(circular_list)):
            # Multiply the current element by the product variable
            product *= circular_list[j]

            # If the product is equal to -46, add the sublist to the list of sublists
            if product == -46:
                sublists.append(circular_list[start:j+1])

    # Return the list of sublists
    return sublists
