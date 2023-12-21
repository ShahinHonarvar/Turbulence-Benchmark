
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the sublist
        product = 1

        # Add the current element to the sublist
        sublist = [circular_list[i]]

        # Iterate through the remaining elements in the circular list
        for j in range(i + 1, len(circular_list)):
            # Multiply the current element by the next element in the circular list
            product *= circular_list[j]

            # If the product equals 33, add the sublist to the list of sublists
            if product == 33:
                sublists.append(sublist)

    # Return the list of sublists
    return sublists
