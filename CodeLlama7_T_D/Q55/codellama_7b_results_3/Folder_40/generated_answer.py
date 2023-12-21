
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Start with the current element and find the next element that has a product equal to -9
        j = i + 1
        while j < len(circular_list) and (circular_list[i] * circular_list[j]) != -9:
            j += 1

        # If we found such an element, add the sublist of contiguous elements to the list of sublists
        if j < len(circular_list):
            sublists.append([circular_list[i], circular_list[j]])

    # Return the list of sublists
    return sublists
