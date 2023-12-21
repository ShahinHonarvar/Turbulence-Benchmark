
def lists_with_product_equal_n(circular_list):
    # Find the maximum product of two elements in the list
    max_product = 0
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i] * circular_list[j]
            if product > max_product:
                max_product = product
    # Initialize an empty list to store the sublists
    sublists = []

    for i in range(len(circular_list)):
        # Find the product of the current element and all subsequent elements
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            if product == max_product:
                # Add the sublist to the list of sublists
                sublists.append(circular_list[i:j + 1])
    return sublists
