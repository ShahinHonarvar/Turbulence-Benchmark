
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Add the current element to the current sublist
        current_sublist = [circular_list[i]]

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):
            # Calculate the product of the elements in the current sublist
            product *= circular_list[j]

            # If the product is equal to -690, add the current sublist to the list of sublists and break out of the loop
            if product == -690:
                sublists.append(current_sublist)
                break

        # If no sublist was added to the list of sublists, continue iterating over the remaining elements of the circular list
        else:
            continue

        # Break out of the loop if a sublist was added to the list of sublists
        break

    # Return the list of sublists
    return sublists
