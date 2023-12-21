
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its adjacent elements
        current_element = circular_list[i]
        left_neighbor = circular_list[(i - 1) % len(circular_list)]
        right_neighbor = circular_list[(i + 1) % len(circular_list)]

        # Calculate the product of the current element and its adjacent elements
        product = current_element * left_neighbor * right_neighbor

        # Check if the product is equal to 46
        if product == 46:
            # If it is, add the sublist containing the current element to the list of sublists
            sublists.append([current_element])

    return sublists
