
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and the next element
        product = 1

        # Calculate the product of the current element and the next element, if there is one
        if i + 1 < len(circular_list):
            product *= circular_list[i] * circular_list[i + 1]

        # If the product is equal to n, add the sublist to the list of sublists
        if product == n:
            sublists.append(circular_list[i:i + 2])

    # Return the list of sublists
    return sublists
