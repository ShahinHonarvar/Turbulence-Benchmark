
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its adjacent elements
        product = 1

        # Multiply the current element by its adjacent elements and store the result in the product variable
        for j in range(i, i + 3):
            product *= circular_list[j]

        # If the product is equal to -46, add the sublist of contiguous integers from the given list to the sublists list
        if product == -46:
            sublists.append(circular_list[i:i + 3])

    # Return the list of sublists
    return sublists
