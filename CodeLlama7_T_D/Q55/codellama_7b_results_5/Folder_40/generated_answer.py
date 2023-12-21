
def lists_with_product_equal_n(circular_list):
    # Find the product of the elements in the list
    product = 1
    for element in circular_list:
        product *= element

    # Check if any sublists have a product equal to -9

    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        if product == -9:
            return [sublist]

    # If no such sublists exist, return an empty list

    return []
