
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):

        # Get the current element and its next element
        curr_elem = circular_list[i]
        next_elem = circular_list[(i + 1) % len(circular_list)]

        # If the product of the current element and its next element is -95, add the sublist to the list of sublists
        if curr_elem * next_elem == -95:
            sublists.append([curr_elem, next_elem])

    return sublists
