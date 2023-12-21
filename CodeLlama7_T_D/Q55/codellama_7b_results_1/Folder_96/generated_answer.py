
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list
    for i in range(len(circular_list)):
        # Get the current element and its successor
        current = circular_list[i]
        next = circular_list[(i+1) % len(circular_list)]

        # Check if the product of the current element and its successor is equal to 0
        if current * next == 0:
            # If so, add the sublist consisting of the two elements to the list of sublists
            sublists.append([current, next])

    # Return the list of sublists
    return sublists
