
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its next element
        element = circular_list[i]
        next_element = circular_list[(i + 1) % len(circular_list)]

        # Check if the product of the current element and its next element is equal to 49
        if element * next_element == 49:
            # If the product is equal to 49, add the current element and its next element to the sublists list
            sublists.append([element, next_element])

    # Return the list of sublists
    return sublists
