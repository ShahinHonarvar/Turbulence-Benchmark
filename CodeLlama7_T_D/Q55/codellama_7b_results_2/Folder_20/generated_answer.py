
def lists_with_product_equal_n(circular_list):
    # Check if the given list is empty or not
    if len(circular_list) == 0:
        return []

    # Initialize a variable to store the sublists with product equal to -69
    sublists = []

    # Iterate through the given circular list and check for sublists with product equal to -69
    for i in range(len(circular_list)):
        current_product = 1

        # Calculate the product of the elements in the sublist starting from the current element
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]

            # If the product equals -69, add the sublist to the list of sublists
            if current_product == -69:
                sublists.append(circular_list[i:j+1])

        # If there are duplicates of such a sublist, they should all be contained in the returned list.
        # To handle this situation, we add each duplicate sublist to the list of sublists
        for sublist in sublists:
            if sublist[0] == circular_list[i]:
                sublists.append(sublist)

    return sublists
