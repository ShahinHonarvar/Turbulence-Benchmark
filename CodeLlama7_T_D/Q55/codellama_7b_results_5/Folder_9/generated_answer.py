
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Get the current element and its next element (wrapped around)
        curr_elem = circular_list[i]
        next_elem = circular_list[(i + 1) % len(circular_list)]

        # If the product of the current element and its next element is equal to -36, add the sublist containing those two elements to the list of sublists
        if curr_elem * next_elem == -36:
            sublists.append([curr_elem, next_elem])

    # Return the list of sublists
    return sublists
