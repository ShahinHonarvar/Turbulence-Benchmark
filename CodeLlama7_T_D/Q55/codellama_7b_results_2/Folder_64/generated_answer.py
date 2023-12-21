
def lists_with_product_equal_n(circular_list):
    # Create an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its adjacent element
        product = 1

        # Check if the current element is not the head of the circular list
        if i != 0:
            # Multiply the current element with its predecessor
            product *= circular_list[i - 1]

        # Check if the current element is not the tail of the circular list
        if i < len(circular_list) - 1:
            # Multiply the current element with its successor
            product *= circular_list[i + 1]

        # If the product is equal to 3, add it to the sublists list
        if product == 3:
            sublists.append([circular_list[i]])

    # Return the sublists list
    return sublists
