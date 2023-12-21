
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with product equal to 247
    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current sublist and its product
        current_sublist = [circular_list[i]]
        current_product = circular_list[i]

        # Iterate through the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):
            # Add the current element to the current sublist
            current_sublist.append(circular_list[j])

            # Calculate the product of the current sublist
            current_product = 1
            for k in range(len(current_sublist)):
                current_product *= current_sublist[k]

            # If the product is equal to 247, add the current sublist to the list of sublists and break out of the loop
            if current_product == 247:
                sublists.append(current_sublist)
                break

    # Return the list of sublists
    return sublists
