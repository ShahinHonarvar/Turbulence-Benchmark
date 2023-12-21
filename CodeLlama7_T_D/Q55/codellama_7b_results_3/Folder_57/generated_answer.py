
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Extract the current element and its adjacent elements
        element = circular_list[i]
        head = circular_list[(i - 1) % len(circular_list)]
        tail = circular_list[(i + 1) % len(circular_list)]
        # Calculate the product of the current element and its adjacent elements
        product = element * head * tail

        # If the product is equal to -75, add the sublist to the list of sublists
        if product == -75:
            sublists.append([element, head, tail])

    return sublists
