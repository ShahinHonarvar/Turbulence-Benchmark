
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list
    for i in range(len(circular_list)):
        # Get the current element and its adjacent elements
        current_element = circular_list[i]
        left_element = circular_list[(i - 1) % len(circular_list)]
        right_element = circular_list[(i + 1) % len(circular_list)]

        # Calculate the product of the current element and its adjacent elements
        product = current_element * left_element * right_element

        # If the product is equal to -89, add the sublist to the list of sublists
        if product == -89:
            sublists.append([current_element, left_element, right_element])

    # Return the list of sublists
    return sublists
