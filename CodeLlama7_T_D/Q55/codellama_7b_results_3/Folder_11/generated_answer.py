
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its adjacent elements
        current_element = circular_list[i]
        previous_element = circular_list[(i - 1) % len(circular_list)]
        next_element = circular_list[(i + 1) % len(circular_list)]

        # Check if the product of the current element and its adjacent elements is equal to -15
        if current_element * previous_element * next_element == -15:
            # Add the sublist to the list of sublists
            sublists.append([current_element, previous_element, next_element])

    # Return the list of sublists
    return sublists
