
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list
    for i in range(len(circular_list)):
        # Get the current element and its successor
        element = circular_list[i]
        successor = circular_list[(i+1) % len(circular_list)]

        # Check if the product of the current element and its successor is equal to -33
        if element * successor == -33:
            # Add the current sublist to the list of sublists
            sublists.append([element, successor])

    # Return the list of sublists
    return sublists
