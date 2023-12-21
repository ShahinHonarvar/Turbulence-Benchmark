
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Start with the current element and find the next element that has a product equal to 45
        curr_elem = circular_list[i]
        j = i + 1
        while j < len(circular_list) and (curr_elem * circular_list[j]) != 45:
            j += 1

        # If we found a sublist with a product equal to 45, add it to the list of sublists
        if j < len(circular_list) and (curr_elem * circular_list[j]) == 45:
            sublists.append([curr_elem] + [circular_list[k] for k in range(i + 1, j + 1)])

    # Return the list of sublists
    return sublists
