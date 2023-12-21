
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    product = 1
    for element in circular_list:
        product *= element

    # Initialize an empty list to store sublists

    sublists = []

    # Iterate over the list and check if each element has a product equal to -938

    for i in range(len(circular_list)):
        current_product = 1
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]
            if current_product == -938:
                sublists.append(circular_list[i:j+1])

    # Return the list of sublists

    return sublists
