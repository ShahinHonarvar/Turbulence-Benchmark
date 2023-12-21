
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its successor
        current_element = circular_list[i]
        if i + 1 < len(circular_list):
            successor_element = circular_list[i + 1]
        else:
            successor_element = circular_list[0]

        # Check if the product of the current element and its successor is equal to 3
        if current_element * successor_element == 3:
            # Add the sublist to the list of sublists
            sublists.append([current_element, successor_element])

    # Return the list of sublists
    return sublists
