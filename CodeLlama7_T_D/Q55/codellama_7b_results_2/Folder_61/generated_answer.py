
def lists_with_product_equal_n(circular_list):
    # Create an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current sublist
        product = 1

        # Add the current element to the current sublist
        sublist.append(circular_list[i])

        # Iterate through the remaining elements of the circular list
        for j in range(i+1, len(circular_list)):
            # Calculate the product of the current sublist and the next element
            product *= circular_list[j]

            # If the product equals -10, add the sublist to the list of sublists and reset the variables
            if product == -10:
                sublists.append(sublist)
                product = 1
                sublist = []

        # Add the last element to the current sublist
        sublist.append(circular_list[i])

    return sublists
