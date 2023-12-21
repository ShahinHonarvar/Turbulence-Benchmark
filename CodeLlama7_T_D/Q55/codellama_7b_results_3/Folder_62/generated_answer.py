
def lists_with_product_equal_n(circular_list):
    # Check if the given list is empty or not
    if len(circular_list) == 0:
        return []

    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the given list
    for i in range(len(circular_list))):
        # Initialize a variable to store the current product
        current_product = 1

        # Initialize a variable to store the size of the current sublist
        current_sublist_size = 0

        # Iterate through the elements of the given list starting from the current element
        for j in range(i, len(circular_list))):
            # Update the product and the size of the current sublist
            current_product *= circular_list[j]
            current_sublist_size += 1

            # Check if the product is equal to n. If so, add the current sublist to the list of sublists
            if current_product == n:
                sublists.append(circular_list[i:j+1])

    return sublists
