
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through the circular list and find contiguous integers with product equal to n
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its next element
        product = circular_list[i] * circular_list[(i+1) % len(circular_list)]

        # If the product is equal to n, add the sublist to the list of sublists
        if product == n:
            sublists.append(circular_list[i: (i+2) % len(circular_list)])

    return sublists
